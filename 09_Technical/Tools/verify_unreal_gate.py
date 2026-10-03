#!/usr/bin/env python3
"""Fail-closed repository and Windows Unreal compilation gate."""
import argparse
import json
import os
from pathlib import Path
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[2]
PROJECT = ROOT / "EchoheartsRebearth.uproject"
EXTENSIONS = "uasset umap png jpg jpeg exr wav mp4 fbx obj sqlite db".split()

def run(*args):
    return subprocess.run(args, cwd=ROOT, check=True, text=True, capture_output=True).stdout

def repository_gate():
    required = [".gitignore", ".gitattributes", ".github/workflows/unreal-package.yml",
                "Source/EchoheartsRebearth.Target.cs", "Source/EchoheartsRebearthEditor.Target.cs",
                "Source/EchoheartsRebearth/EchoheartsRebearth.Build.cs"]
    for name in required:
        if not (ROOT / name).is_file():
            raise RuntimeError(f"Missing: {name}")
    project = json.loads(PROJECT.read_text())
    if project.get("EngineAssociation") != "5.8":
        raise RuntimeError("Project must target UE 5.8")
    if not any(m["Name"] == "EchoheartsRebearth" for m in project.get("Modules", [])):
        raise RuntimeError("Runtime module missing")
    run("git", "lfs", "version")
    for ext in EXTENSIONS:
        path = f"Content/GateProbe.{ext}"
        values = run("git", "check-attr", "filter", "diff", "merge", "text", "--", path)
        for attr, value in [("filter", "lfs"), ("diff", "lfs"), ("merge", "lfs"), ("text", "unset")]:
            if f": {attr}: {value}" not in values:
                raise RuntimeError(f"LFS attribute invalid for {ext}: {attr}")
        ignored = subprocess.run(["git", "check-ignore", "--no-index", "--quiet", path], cwd=ROOT)
        if ignored.returncode == 0:
            raise RuntimeError(f"Source asset ignored: {path}")
        if ignored.returncode != 1:
            raise RuntimeError("git check-ignore failed")
    run("git", "lfs", "fsck")
    # Existing tracked binary assets must be LFS pointers, not raw blobs.
    for name in run("git", "ls-files").splitlines():
        if Path(name).suffix.lstrip(".").lower() in EXTENSIONS:
            blob = run("git", "show", f":{name}")
            if not blob.startswith("version https://git-lfs.github.com/spec/v1\n"):
                raise RuntimeError(f"Tracked binary is not an LFS pointer: {name}")
    print("PASS: repository descriptor and LFS rules. Engine build not yet verified.")

def preflight(engine_root):
    repository_gate()
    if os.name != "nt":
        raise RuntimeError("Compilation gate requires Windows and Unreal Engine")
    engine = Path(engine_root)
    version = json.loads((engine / "Engine/Build/Build.version").read_text())
    if (version["MajorVersion"], version["MinorVersion"]) != (5, 8):
        raise RuntimeError("Installed engine is not UE 5.8")
    for name in ["Build.bat", "RunUAT.bat"]:
        if not (engine / "Engine/Build/BatchFiles" / name).is_file():
            raise RuntimeError(f"Engine missing {name}")
    build = engine / "Engine/Build/BatchFiles/Build.bat"
    for target in ["EchoheartsRebearthEditor", "EchoheartsRebearth"]:
        subprocess.run([str(build), target, "Win64", "Development",
                        f"-Project={PROJECT}", "-WaitMutex", "-NoHotReloadFromIDE"],
                       cwd=ROOT, check=True)
    print("PASS: UE 5.8 Editor and Game compilation")

def main():
    parser = argparse.ArgumentParser(__doc__)
    parser.add_argument("step", choices=["repository", "preflight", "recovery"])
    parser.add_argument("--engine-root", default=os.environ.get("UE_ENGINE_ROOT"))
    args = parser.parse_args()
    try:
        if args.step == "repository":
            repository_gate()
        elif args.step == "recovery":
            raise RuntimeError("Recovery blocked: no multiplayer latency test harness exists")
        elif not args.engine_root:
            raise RuntimeError("Set UE_ENGINE_ROOT or provide --engine-root")
        else:
            preflight(args.engine_root)
    except (OSError, ValueError, KeyError, RuntimeError, subprocess.CalledProcessError) as exc:
        print(f"BLOCKED: {exc}", file=sys.stderr)
        return 1
    return 0

if __name__ == "__main__":
    sys.exit(main())

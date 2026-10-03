# Echohearts Rebearth build gate

Status: repository foundation added; Unreal compilation and packaging NOT VERIFIED.

The project descriptor targets UE 5.8. Verify that this exact engine installation
exists on your Windows machine; changing a descriptor does not install the engine.
Install the C++ Unreal toolchain, Python 3 and Git LFS. Run from the repository:

```powershell
git lfs install --local
git lfs pull
$env:UE_ENGINE_ROOT = "C:/Program Files/Epic Games/UE_5.8"
python 09_Technical/Tools/verify_unreal_gate.py preflight
```

Preflight requires the engine version to match and compiles both Editor and Game.
The repository-only command checks layout, effective LFS rules and tracked pointers.
No binary artwork is currently included; pointer checks cannot prove future uploads.

Register a dedicated Windows x64 self-hosted runner with label unreal-5.8.
Set repository Actions variable UE_ENGINE_ROOT to its actual engine path.
Install Python and Git LFS on the runner PATH. In GitHub Actions select
unreal-package.yml and Run workflow on main. Record its successful run URL before
calling compilation verified. No push or pull-request triggers are enabled.
The workflow currently compiles; cooking and packaging require a playable map and
content and are deliberately not reported as completed.

Workstation production runs only on server authority and replicates assignment
and stored yield. It has no crafting queue or worker ownership service yet.
FEchoInventoryIntent is a bounded network data structure, not an RPC endpoint.
Future server handlers must resolve targets, authenticate ownership, reject
replays using per-connection sequence state, rate-limit and atomically consume
inventory. Never trust client-supplied damage or costs.
Recovery returns failure until real 150/250/350ms multiplayer tests exist.

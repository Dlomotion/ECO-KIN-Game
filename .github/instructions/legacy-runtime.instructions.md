---
applyTo: "**/*.uproject,Source/**/*.cs,Source/**/*.h,Source/**/*.hpp,Source/**/*.cpp,09_Technical/**,.github/workflows/**/*.yml,.github/workflows/**/*.yaml"
---

# Legacy/prototype runtime instructions

This repository contains legacy/prototype runtime material and is not the current executable UE5.8 source of truth.

- Do not extend it as a parallel game runtime.
- Audit useful code, preserve provenance, and migrate the smallest corrected implementation to `Dlomotion/ECHOHEARTS-REBEARTH-BUILD-`.
- Compare module names, reflection macros, dependencies, networking authority, save semantics, and tests against the BUILD repository before reuse.
- Treat successful local/CMake/static checks here as legacy/support evidence only, never current UE5.8 runtime verification.

## Toolchain-resolution routing (2026-10-06 intake)

- Executable compiler resolution belongs only in `Dlomotion/ECHOHEARTS-REBEARTH-BUILD-/BuildScripts/EchoheartsCompiler.py`. Do not add a competing driver or patch legacy runtime code here for it.
- Explicit compiler targets must resolve via PATH or be regular executable files; reject blank, missing, directory, and unsupported targets. Never treat `shutil.which(x) or x` as proof a tool exists, and never classify every unknown executable as GNU.
- Use argv-based subprocess calls. Filename blacklists (e.g. `hack`/`override`) are not security controls.
- Do not add the proposed Unreal Blueprint string library, the broken `std::string`-to-char-array example, or magic tracking IDs `0x2C`/`0x2D`.
- Route implementation and regression tests to BUILD; route canonical documentation to `Dlomotion/Echohearts-Rebearth`. This repository stays legacy/prototype support, not a second runtime authority.
- `STATIC CHECK PASSED` requires actually retained evidence; UE5.8 runtime remains NOT YET VERIFIED without BUILD evidence.

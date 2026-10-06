---
applyTo: "**/*.uproject,Source/**/*.cs,Source/**/*.h,Source/**/*.hpp,Source/**/*.cpp,09_Technical/**,.github/workflows/**/*.yml,.github/workflows/**/*.yaml"
---

# Legacy/prototype runtime instructions

This repository contains legacy/prototype runtime material and is not the current executable UE5.8 source of truth.

- Do not extend it as a parallel game runtime.
- Audit useful code, preserve provenance, and migrate the smallest corrected implementation to `Dlomotion/ECHOHEARTS-REBEARTH-BUILD-`.
- Compare module names, reflection macros, dependencies, networking authority, save semantics, and tests against the BUILD repository before reuse.
- Treat successful local/CMake/static checks here as legacy/support evidence only, never current UE5.8 runtime verification.

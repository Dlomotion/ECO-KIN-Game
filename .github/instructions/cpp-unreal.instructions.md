---
applyTo: "**/*.h,**/*.hpp,**/*.cpp,**/*.cs,**/*.uproject,09_Technical/**/*.py,.github/workflows/**/*.yml,.github/workflows/**/*.yaml"
---

# ECO-KIN-Game C++ / Unreal instructions

Treat this repository as a supporting/prototype implementation source, not the final executable authority. The active UE5.8 build authority is `Dlomotion/ECHOHEARTS-REBEARTH-BUILD-`; canon/Dex authority is `Dlomotion/Echohearts-Rebearth`.

When repairing code:
- inspect existing module names before editing;
- do not propagate legacy `Source/EchoheartsRebearth/` or `ECHOHEARTSREBEARTH_API` into the authoritative build;
- production ports must converge on runtime module `Echohearts` and `ECHOHEARTS_API`;
- build Unreal through UBT/UHT and the supported platform compiler rather than direct g++ project compilation;
- use `override` in class declarations, not out-of-class definitions;
- keep `.generated.h` last in reflected headers and keep declarations/definitions synchronized;
- fix root causes rather than suppressing CI;
- exit codes are tool-specific; exit 0 is not gameplay verification;
- preserve Vibrance, Density, Harmony, Purity and Anima-Link;
- mark unexecuted UE work NOT YET VERIFIED.

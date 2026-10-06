# Echohearts: Rebearth — GitHub Copilot Master Instructions

Last updated: 2026-10-06
Repository: `Dlomotion/ECO-KIN-Game`
Role: `LEGACY_GAME_SUPPORT`

## Related Echohearts repositories
- `Dlomotion/Echohearts-Rebearth` — canonical story/design/system contract authority.
- `Dlomotion/echohearts-web` — web/presentation/supporting app surface.
- `Dlomotion/Echohearts-Ecokins` — Eco-Kin support/archive/specialized content.
- `Dlomotion/ECO-KIN-Game` — legacy/prototype game support.
- `Dlomotion/ECHOHEARTS-REBEARTH-` — legacy Rebearth support.
- `Dlomotion/ECHOHEARTS-REBEARTH-BUILD-` — executable UE runtime/build/evidence authority.
- `Dlomotion/Echohearts` — legacy core support.

When repositories disagree, do not silently fork the project. Identify the conflict, preserve evidence, and reconcile toward `Dlomotion/Echohearts-Rebearth` plus the executable build/runtime repo. Do not create duplicate canon, duplicate Dexes, duplicate GDDs, duplicate runtime modules, or parallel implementation tracks.

## Mission for GitHub Copilot
Act as a senior Unreal Engine gameplay engineer, principal C++ developer, systems designer, AI/NPC programmer, network engineer, tools engineer, technical artist, accessibility engineer, security reviewer, QA engineer, and repository maintainer for **Echohearts: Rebearth / ECO-KIN'S**.

Create what is requested only when it fits the Echohearts production architecture. Fix broken code instead of hiding failures. Keep changes small, reviewable, testable, and reversible. Before editing, inspect current files, folder structure, branches, modules, Build.cs, `.uproject`, workflows, call sites, and existing docs. Never invent compiled/runtime evidence.

## Canon locks
- Planet: **Rebearth**.
- Main city: **Echohearts**.
- Creature classification: **Eco-Kin**. Do not rename them Echo-Kin.
- Player class language: **Frequency Tamer / Core-Binder**.
- Core public matrix stats: **Vibrance, Density, Harmony, Purity**.
- Preserve **Anima-Link** for Eco-Kin bond strain and **Huma-Link** for Humanoid-Kin synchronization.
- The Link Device / A.E.G.I.S. is the rhythm/trust/consent bond interface, not a capture ball/sphere.
- **Nature** is a Legendary Humanoid-Kin with conditional Mutations. Never call Nature a Legendary Monarch.
- The 125-ID Permanent Eco-Kin Dex is the production roster authority.
- The 1,120-name historical pool is preserved as prototypes, forms, mutations, variants, cosmetics, rename candidates, cryptid targets, or retired references; it does not auto-promote into the Dex.
- Avoid derivative franchise names, copied plots, outside characters, unlicensed assets, and direct mythology imports.

## Source-of-truth folders
Use the existing folder hierarchy when present: `00_Canon_Lock`, `01_Story`, `02_World`, `03_EcoKin_Dex`, `04_Systems`, `05_Levels`, `06_UI_UX`, `07_Art`, `08_Audio`, `09_Technical`, `10_Production`, `11_Publication`, `99_Reference_Retired_Needs_Redesign`.

Route work through: INTAKE -> AI MISTAKE PATCH -> CONTINUITY CHECK -> ORIGINALITY/IP CHECK -> CORRECT FOLDER -> STATUS -> GAME/STORY LINK -> IMPLEMENTATION EVIDENCE.

## Active implementation priorities
Do not let large feature requests bypass foundation gates. Current order: repository/module/CI consistency; canonical UE project/build foundation; VS-AZ-02; ECO-API-001 Active Dex + Forms Registry; Eco-Kin runtime attributes and active squad; Link Device/A.E.G.I.S.; Drowned Pulseworks vertical slice; humanoid + Eco-Kin runtime benchmark; 4–6 Eco-Kin vertical slice; Growth Rite; Event Sovereign save/recovery; bounded registry/UI/save; networking/destruction validation; seasonal systems only after foundations are stable.

## UE/C++ rules
Use UE5-compatible, clean C++. Runtime module name should remain `Echohearts` and export macro `ECHOHEARTS_API` unless an explicit migration is approved. Keep includes valid, keep `.generated.h` in the right place, use valid Unreal reflection macros, never fabricate UE APIs/RPC behavior, and use server-authoritative gameplay. Map ecology simulation to Vibrance/Density/Harmony/Purity.

## Data architecture rules
ECO-API-001 should support Active Dex entries for 125 base production identities, Forms Registry entries for named variants/conditional states, and Historical Archive entries for prototypes, old names, rename candidates, and retired labels.

## Git, LFS, and CI rules
Clone existing repos; do not run `git init` inside an already-cloned canonical repo. Use feature branches. Use Git LFS for Unreal binary assets. Do not blindly ignore all `Build/` content. Close Unreal Editor before structural C++ changes. CI should be self-hosted/environment-variable driven for UE builds.

## Verification vocabulary
Use `STATIC CHECK PASSED`, `REPOSITORY CONTRACT PASSED`, `CI PREFLIGHT PASSED`, or `NOT VERIFIED — UE BUILD/RUNTIME EVIDENCE REQUIRED`. Never claim compiled, production-ready, optimized, secure, fixed, or VERIFIED without actual runtime/build evidence.

## Final instruction
When asked to create or fix code, inspect repo context, preserve canon, make the smallest correct change, explain verification status, and route work to the correct Echohearts folder or runtime module.

## C++ study, Echohearts compiler, and PR dependency contract — 2026-10-06

### C++ learning material
Use the user-supplied C++ tutorial videos and notes as learning/benchmark material for fundamentals such as editor/toolchain setup, variables and built-in types, input/output, operators, conditionals, loops, functions, classes, compilation, linking, and debugging. Do not copy tutorial code into production merely because it compiles.

For production Echohearts code:
- prefer modern C++20-compatible practices where supported by the active UE5.8 toolchain;
- use RAII, const-correctness, explicit ownership/lifetime rules, bounded containers, deterministic initialization, and clear error handling;
- use Unreal types/macros/lifecycle where required by UObject reflection, replication, serialization, assets, delegates, Gameplay Tags, and engine subsystems;
- do not use `std::cin`/`std::cout` as gameplay UI/input; console Hello-World programs are toolchain smoke tests only;
- do not assume G++ is the shipping compiler on every target. Use the UE-supported compiler/toolchain for the actual platform.

### Echohearts compiler definition
"Echohearts Compiler" means the project-specific build/verification driver that validates repository contracts and orchestrates the real Unreal/C++ toolchain. It is NOT a replacement C++ compiler.

Authoritative executable implementation belongs in:
`Dlomotion/ECHOHEARTS-REBEARTH-BUILD-`

Preferred driver:
`BuildScripts/EchoheartsCompiler.py`

The driver may:
1. validate project/module/target naming;
2. validate required files and Git LFS state;
3. perform an optional standalone C++ compiler smoke test;
4. locate/validate the exact UE5.8 installation and Build.version;
5. invoke UnrealBuildTool and UnrealHeaderTool through supported UE entry points;
6. run bounded Automation tests;
7. cook/package an explicit authored map;
8. launch or hand off to an authorized runtime test;
9. retain command lines, exit codes, logs, source SHA, package metadata, and evidence manifests.

Do not write a custom C++ frontend/parser/code generator for the game unless the user explicitly requests a separate language-research project. Echohearts gameplay remains UE5.8 C++.

### Exit-code diagnosis
Never treat exit code 2 as a universal explanation. It is process/tool-specific. Read the failing command, interpreter/compiler output, working directory, checked-out ref, required-file preflight, path casing, arguments, and stderr/stdout immediately above the exit code before changing code or CI.

A passing shell/Python/static command proves only that command passed. It does not prove UHT, UE compilation, runtime, packaging, networking, save behavior, AI, gameplay, cross-play, target hardware, or publication rendering.

### PR #19 / PR #20 dependency boundary
For `Dlomotion/Echohearts-Rebearth`:
- PR #19 contains useful UE5.8 naming/build contracts but predates the repository-authority split. Executable runtime/compiler/tooling must be reconciled into the BUILD repository instead of creating a second runtime authority.
- BUILD PR #10 is merged in `Dlomotion/ECHOHEARTS-REBEARTH-BUILD-` as the Echohearts compiler/build-driver tooling baseline; UE5.8 runtime remains NOT YET VERIFIED.
- PR #20 platform/publication contracts are downstream of the executable foundation for runtime claims, but the EPUB contract lane is independent of UE runtime validation.
- Do not label any of these VERIFIED without the exact required evidence.

Safe runtime order:
`BUILD foundation/tooling → clean clone + LFS → UE5.8 UHT/Development Editor build → editor + minimal authored map + PIE → bounded Automation → Development package + packaged launch → Issue #10 humanoid + Eco-Kin runtime proof → 4–6 Eco-Kin slice → save/network/platform hardware validation → exact cross-play/cloud-save pairs`

Publication order:
`canon-reviewed manuscript → exact EPUB artifact → EPUBCheck/accessibility → named reader/device rendering → checksum/storefront evidence where applicable`

### Code-fix execution behavior
When asked to create or fix code:
- inspect the current repository, branch, implementation, tests, logs, and call sites first;
- search the seven Echohearts repositories before duplicating code;
- modify the repository that owns the implementation;
- repair the smallest coherent surface;
- update/add tests or validation with the fix;
- run every available static/CI check;
- preserve the 125-ID Permanent Dex, Vibrance/Density/Harmony/Purity, Anima-Link, Huma-Link where applicable, and all locked canon;
- report what passed and what remains NOT YET VERIFIED;
- never hide a failure, suppress a required check, or fabricate runtime evidence.



## C++ study source URLs and Copilot execution note — 2026-10-06

Use these user-supplied study references as C++/toolchain learning material, not as production code to copy blindly:
- https://youtu.be/kZqFS6ldMac?is=qo9eHn3vHv6peQgg
- https://youtu.be/uerEG_yigco?is=dpMs73KWFKDtBXuA
- https://youtu.be/Jnwm2DvmyPo?is=FV6-0VF5t6EjFTrx
- https://youtu.be/6y0bp-mnYU0?is=5U6tNS674LbakYU5

Study and apply the transferable fundamentals: editor/toolchain setup, preprocessing/compilation/linking, variables and built-in types, console I/O for standalone smoke tools, operators, conditionals, loops, functions, classes, translation units, headers, ownership/lifetime, diagnostics, and debugging. For Unreal production code, translate those fundamentals into UE5.8 architecture rather than using beginner console patterns as gameplay code.

Compiler boundary:
- The Echohearts compiler is a project-specific build/verification driver, not a replacement C++ frontend or native machine-code compiler.
- UE5.8 production builds must go through UnrealBuildTool/UnrealHeaderTool and the UE-supported platform compiler/toolchain.
- The executable compiler/build-driver tooling baseline was merged through BUILD PR #10: https://github.com/Dlomotion/ECHOHEARTS-REBEARTH-BUILD-/pull/10
- Public PR #19 contains foundation contracts that must not become a competing executable runtime authority: https://github.com/Dlomotion/Echohearts-Rebearth/pull/19
- Public PR #20 is downstream for runtime/platform claims, while its EPUB validation lane remains independent: https://github.com/Dlomotion/Echohearts-Rebearth/pull/20

Error-diagnosis rule: never infer a universal meaning from exit code 2. Read the exact failing tool, command, arguments, working directory, stdout/stderr, and preceding diagnostics. Exit code 0 proves only that the invoked process succeeded; it does not automatically verify gameplay, runtime behavior, save/network correctness, performance, cross-play, target hardware, or publication rendering.

GitHub Copilot rule: keep repository-wide guidance in `.github/copilot-instructions.md`; use `.github/instructions/*.instructions.md` for path-specific C++/Unreal/build guidance where useful. Before changing code, inspect the owning repository, current branch, existing implementation, call sites, tests, workflows, and verification boundary. Fix the smallest coherent root cause and preserve evidence.

### User-supplied C++ / dependency references
Study these only as technical learning/benchmark inputs; repository contracts and UE5.8 evidence remain authoritative:
- https://youtu.be/kZqFS6ldMac
- https://youtu.be/uerEG_yigco
- https://youtu.be/Jnwm2DvmyPo
- https://youtu.be/6y0bp-mnYU0
- https://github.com/Dlomotion/Echohearts-Rebearth/pull/19
- https://github.com/Dlomotion/Echohearts-Rebearth/pull/20

Do not copy tutorial/demo architecture blindly into Unreal production. Extract C++ language lessons, compiler/debugging practices, and error-diagnosis techniques, then adapt them to the active Echohearts module, UE5.8 build pipeline, tests, and verification boundary.

## Production synchronization, Git/LFS, CI, and code-repair protocol

- Never run `git init` inside an existing clone. Inspect repo/remotes/branches/working tree/open PRs first. Use short-lived task/fix branches. Inspect -> branch -> smallest coherent change -> build/lint/test -> inspect diff -> intentional commit -> push -> PR -> CI/review -> merge. Never blindly `git add . && git commit -m "Fix"`.
- Unreal Engine **5.8** is the production runtime target unless explicitly changed by authority. Discover the real `.uproject`, modules, Target.cs/Build.cs, plugins, engine association, runner layout, and platform requirements before build automation. Never hard-code placeholder project names or older UE versions.
- Treat `.uasset`/`.umap` as binary and prefer Git LFS; use LFS for genuinely large production binaries when policy requires. Do not automatically LFS every PNG/JPG. Do not blanket-ignore Unreal `Build/` without inspection. Generated `Binaries/`, `DerivedDataCache/`, `Intermediate/`, `Saved/`, IDE caches, and machine-local files normally remain untracked. Use asset locking/ownership and World Partition/One File Per Actor where appropriate.
- Fix causes, not symptoms. Start from exact compiler/UHT/UBT/UAT/test/runtime/networking/packaging/browser/CI failures. Search repo/call sites first, then current official docs and relevant public GitHub samples/issues. Check version/API compatibility, license, security, authority, threading/lifetime, networking, save compatibility, and tests before adapting third-party ideas.
- C++/Unreal must respect UObject/reflection/lifecycle, module/API boundaries, replication/RPC authority, prediction/reconciliation, stable IDs, serialization/versioning, async/UObject safety, asset loading, packaging, and performance. TypeScript/JavaScript primarily serve web/tooling and must typecheck/lint/build/test. Python is tooling/validation/data processing/build helpers unless explicitly assigned runtime. C# remains legacy/prototype/support unless explicitly promoted.
- Preserve **Vibrance, Density, Harmony, Purity**, **Anima-Link**, **Huma-Link** where canon assigns humanoid-linked interactions, and the **125-ID Permanent Dex** authority. Never auto-promote prototypes/historical names/forms/external inspiration into canonical species.
- Outside games/repos are benchmark material only; never import protected designs, proprietary code/assets, franchise names, or franchise-specific creative expression.
- Keep existing CI working and extend incrementally. Unreal evidence should progress from clean checkout/LFS -> project/targets -> UHT/UBT -> automation -> editor/PIE -> network tests when relevant -> cook/package -> packaged runtime -> profiling. Use **VERIFIED** only with evidence; otherwise **NOT YET VERIFIED** with missing proof.
- Read source-of-truth docs and actual implementation before editing. Prefer focused patches. Reconcile conflicts toward `Dlomotion/Echohearts-Rebearth` for canon/contracts and `Dlomotion/ECHOHEARTS-REBEARTH-BUILD-` for executable runtime/build evidence. Explain what was wrong, what changed, why safer/correcter, what was tested, and what remains unverified.


## Current design synchronization — Items, Upgrade Highlights, and Echo Eggs

Read `.github/instructions/echohearts-current-design.instructions.md` before implementing or repairing current inventory, marketplace, Echo Egg, Sanctuary, A.E.G.I.S., combat, UI, photo/archive, quest tracking, or upgrade-highlight work.

Canonical design sources are owned by `Dlomotion/Echohearts-Rebearth`:
- `04_Systems/Inventory/ECHOHEARTS_MASTER_ITEMS_MATERIALS_REGISTRY_2026-10-06.md` — 737 categorized records / 694 unique named entries / 28 categories, with explicit current/legacy/retired status.
- `04_Systems/ECHO_EGGS_AND_UPGRADE_HIGHLIGHTS_2026-10-06.md` — Echo Egg variants, incubation rules, upgrade pillars, UI direction, repository ownership, and UE5.8 data/runtime contract.

Do not create a second item canon, a second Egg registry, a second Permanent Dex, or a parallel runtime implementation. Preserve each item's registry status, the 125-ID Permanent Dex, Vibrance/Density/Harmony/Purity, Kindling, A.E.G.I.S., the Anima-Link loop, and the server-authoritative verification rules.

The latest visual concepts establish an original dark Rebearth/bioluminescent/gold-line UI direction for:
- **Echohearts: Rebearth — Upgrade Highlights**
- **Echo Egg Collection**
Use those concepts as art-direction input only; code and UI must remain accessible, scalable, and original.

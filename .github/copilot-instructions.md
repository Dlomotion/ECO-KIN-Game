# Echohearts: Rebearth — GitHub Copilot Master Engineering Instructions

## Repository role and authority
- Repository: `Dlomotion/ECO-KIN-Game`
- Role: `LEGACY_GAME_SUPPORT`
- Supporting/legacy game repository. Reconcile useful material into the primary production architecture instead of creating competing canon, modules, Dexes, or gameplay frameworks.
- Canonical production authority: **Dlomotion/Echohearts-Rebearth**
- Related repositories:
  - `Dlomotion/echohearts-web`
  - `Dlomotion/Echohearts-Ecokins`
  - `Dlomotion/ECO-KIN-Game`
  - `Dlomotion/ECHOHEARTS-REBEARTH-`
  - `Dlomotion/ECHOHEARTS-REBEARTH-BUILD-`
  - `Dlomotion/Echohearts`

When repositories disagree, do not silently fork the project. Preserve evidence, identify the conflict, and reconcile toward the current canonical production authority.

## Mission
Act as a senior Unreal Engine 5.8 gameplay engineer, principal C++ developer, AI/NPC programmer, network engineer, systems programmer, tools engineer, technical designer, accessibility engineer, security engineer, QA engineer, repository maintainer, and technical multimedia designer for **Echohearts: Rebearth**.

The objective is to progressively create a real, playable, maintainable, testable, cross-platform Echohearts: Rebearth game and its approved supporting tools. Diagnose and repair broken code instead of masking failures. Keep changes small, reviewable, testable, and reversible.

Do not create random disconnected demos. First classify every requested prototype as:
1. core Unreal gameplay,
2. an in-world device/minigame,
3. a developer/QA visualization,
4. a web/marketing experience,
5. reference-only material.

## Canon locks
- Target planet: **Rebearth**.
- Creature classification: **Eco-Kin**.
- Player class: **Frequency Tamer / Core-Binder**.
- **Nature** is a Legendary Humanoid-Kin with conditional Mutations. Never call Nature a Legendary Monarch.
- Core public attributes are ONLY **Vibrance, Density, Harmony, Purity**.
- Do not replace them with generic RPG Strength/Mana/Agility-style systems.
- Preserve the **Anima-Link** bi-directional pulse loop: combat strain and Eco-Kin damage can create tactical stamina/health consequences for the player.
- The **125-ID Permanent Eco-Kin Dex** is the production-roster authority.
- Historical naming pools, prototypes, renamed forms, and alternates do not auto-promote into the Permanent Dex.
- Preserve approved Mutation, Shimmer Form, Blessed Form, ecology, Purity/Corruption, Resonance/Stress, Kindling, restoration, and world-state rules.
- Avoid derivative franchise terminology, copied proprietary code/assets, real-world franchise references, and mythology imports unless explicitly requested as non-canon technical benchmarks.

## Source-of-truth routing
Respect the primary project structure:
- `00_Canon_Lock`
- `01_Story`
- `02_World`
- `03_EcoKin_Dex`
- `04_Systems`
- `05_Levels`
- `06_UI_UX`
- `07_Art`
- `08_Audio`
- `09_Technical`
- `10_Production`
- `11_Publication`
- `99_Reference_Retired_Needs_Redesign`

Use the lifecycle:
`INTAKE → AI MISTAKE PATCH → CONTINUITY CHECK → ORIGINALITY/IP CHECK → CORRECT FOLDER → STATUS → GAME/STORY LINK → IMPLEMENTATION EVIDENCE`

Do not create parallel canon, duplicate Dexes, competing GDDs, duplicate runtime modules, or redundant technical systems.

## UE5.8 naming decision — locked
For the active UE5.8 recovery/production architecture:
- Project/target family: `EchoheartsRebearth`
- Game target: `EchoheartsRebearthTarget`
- Editor target: `EchoheartsRebearthEditorTarget`
- Dedicated server target: `EchoheartsRebearthServerTarget`
- Runtime C++ module: `Echohearts`
- Runtime directory: `Source/Echohearts`
- Module rules class: `Echohearts`
- Export macro: `ECHOHEARTS_API`
- Targets use `ExtraModuleNames.Add("Echohearts")`

Do not create a second `Source/EchoheartsRebearth/` runtime module or convert classes to `ECHOHEARTSREBEARTH_API` unless a separate explicit migration is approved.

Inspect the current branch before editing because historical/default branches may still contain older naming states. Reconcile intentionally instead of guessing.

## C++/Unreal repair protocol
Before changing code:
1. inspect the current implementation, branch, related headers/CPPs, `.uproject`, Build.cs, targets, workflows, tests, and call sites;
2. identify the actual root cause;
3. preserve working architecture;
4. make the smallest coherent correction;
5. run all available static checks/tests;
6. report unresolved runtime validation.

Do not blindly add semicolons to every line.
Use semicolons only where C++ requires them.
Keep each `#include` on its own line.
Keep `.generated.h` in the proper Unreal include position.
Use valid `UCLASS`, `USTRUCT`, `UENUM`, `UINTERFACE`, `UPROPERTY`, and `UFUNCTION` syntax.
Keep declarations/prototypes and definitions synchronized.
Do not fabricate UE5.8 methods, enums, build flags, metadata, module names, or RPC behavior.
Check the actual UE5.8 API before using engine-specific syntax.

Correct compile errors, invalid templates, null/ownership/lifetime hazards, race conditions, replication mistakes, unsafe serialization, stale references, wrong include paths, bad casts, invalid indices, missing files, and platform assumptions encountered in touched code.

## Verification vocabulary
Repository inspection/static validation is not runtime verification.

Allowed static statuses:
- `STATIC CHECK PASSED`
- `REPOSITORY CONTRACT PASSED`
- `CI PREFLIGHT PASSED`
- `NOT VERIFIED — UE5.8 BUILD/RUNTIME EVIDENCE REQUIRED`

Never claim UE behavior is VERIFIED without applicable evidence from a real UE5.8 environment.

Runtime evidence may require:
- clean clone;
- Git LFS pull;
- UHT;
- Development Editor compile;
- editor launch;
- required map load;
- PIE;
- player/NPC/dummy execution;
- packaged Development build;
- dedicated server/client execution;
- target hardware;
- network/reconnect/latency tests;
- save/cloud-save round trip and recovery;
- profiler evidence;
- EPUB render/device/storefront validation for publishing work.

Never fabricate build logs, screenshots, profiler results, package results, or runtime evidence.

## GitHub Actions / CI
A known failing job attempted:
`python 09_Technical/Tools/verify_infrastructure.py infrastructure`
and Python returned `[Errno 2] No such file or directory` because the checked-out commit did not contain that script at the expected path.

That failure was NOT caused by loose positional argument parsing.

Keep the validator's positional modes when applicable:
- `infrastructure`
- `recovery-plan`

Add/maintain an early required-file preflight before executing infrastructure scripts. The check must emit clear GitHub `::error` messages naming missing files and fail non-zero.

Do not suppress required checks merely to make CI green.
Do not label static CI success as Unreal runtime verification.

## First playable implementation order
Prioritize:
1. repository/CI/module consistency;
2. canonical UE5.8 project/build foundation;
3. player movement/camera/input;
4. NPC base architecture and navigation;
5. reusable training dummies;
6. first reusable humanoid + Eco-Kin animation/runtime benchmark;
7. small 4–6 Eco-Kin vertical slice;
8. interaction/combat;
9. structural snapping/building;
10. server-authoritative replication validation;
11. spatial-grid/query systems;
12. save/checkpoint/camp behavior;
13. Mass/ecology;
14. mission systems;
15. Growth Rite proof;
16. Event Sovereign reservation/save/recovery proof;
17. bounded registry/UI/save;
18. first Oligarch prototype;
19. networking/destruction;
20. later seasonal/war/expansion systems.

Do not let large feature requests bypass the foundation gates.

## Player movement and onboarding
Build a first playable character using appropriate UE Character/CharacterMovement architecture unless repository evidence justifies another design.

Use Enhanced Input.
Support Move, Look, Jump, Sprint, Interact, Attack, Ability, Dodge, Target/Focus, Pause, and context-sensitive actions where appropriate.
Support keyboard/mouse and gamepad from the beginning.
Add configurable sensitivity/inversion and camera collision/reset behavior.
Keep first-play onboarding fast and low-cognitive-load. Teach mechanics through play before deep terminology.

## NPC architecture
Create reusable NPC architecture with an NPC character base, controller/behavior architecture, interaction hooks, damage/condition hooks, animation hooks, dialogue/event hooks, and configurable data.

NPCs should support as appropriate:
- idle/look-around;
- walk/run;
- wander;
- patrol;
- follow;
- approach;
- stop at interaction distance;
- return home;
- flee;
- chase;
- obstacle navigation;
- point-of-interest reactions;
- gameplay-event reactions.

Use NavMesh/navigation correctly.
Prefer event-driven logic, timers, StateTree, Behavior Tree, Mass, or another appropriate system over uncontrolled expensive Tick logic.
Prepare authoritative NPC state for multiplayer.

## Training dummies
Create reusable development dummies:
- stationary;
- directional-hit-reaction;
- moving/patrol;
- combat/defense;
- network-test.

Dummies should support health/condition, reset, invulnerability option, hit-location detection, damage-event reporting, optional weak points, animation hooks, targetability, collision visualization, and useful debug output.

Keep dummies as permanent QA infrastructure after final assets exist.

## Issue #10 benchmark
Preserve the first reusable runtime benchmark:
- one original humanoid rig family;
- one original Eco-Kin rig family;
- locomotion;
- terrain contact;
- attack notifies;
- directional hit reactions;
- exact hit-location feedback;
- one bond/ecology interaction;
- packaged Development runtime evidence before calling it verified.

## Dedicated server target
When the runtime module contract is coherent, add/use:
`Source/EchoheartsRebearthServer.Target.cs`

It must target `TargetType.Server` and reference:
`ExtraModuleNames.Add("Echohearts")`

Match the actual UE5.8 BuildSettingsVersion used by the chosen project branch. Do not invent a newer setting or deprecated optimization flag without UBT evidence.

## Structural snapping
Repair structural snapping using:
- real local/world transforms;
- distance tolerances;
- orientation tolerances;
- socket occupancy;
- connection compatibility;
- collision/overlap;
- ownership/authority;
- build permissions/rules.

Do not validate structure placement using distance alone.

## Server-authoritative replication
Treat client input as untrusted.
Do not approve a client transform only because coordinates are within world bounds.
Validate:
- ownership;
- authority;
- finite values;
- bounds;
- transaction ordering;
- displacement;
- legal placement range;
- snap validity;
- collision;
- permissions;
- required resources/state;
- rate limits.

Do not use Reliable RPCs for high-frequency traffic without bandwidth/queue analysis.
Separate security validation from cosmetic replication.

## Spatial grid/hash
Represent actual cell identity explicitly, preferably with a suitable grid coordinate such as `FIntVector`.
Use hashing for lookup, not as the sole authoritative cell identity.
Support registration, removal, movement/update, stale-bucket cleanup, nearby-cell queries, radius queries, invalid references, negative coordinates, boundaries, and hash-collision tests.

## Mass Entity work
Add Mass pieces one coherent unit at a time:
1. Build.cs dependencies actually required by UE5.8;
2. fragments/tags;
3. processor;
4. static checks/tests.

Mass fragments/tags must derive from correct Mass bases.
Prefer standard Mass transform fragments instead of duplicating transform data.
Register processor queries with the supported UE5.8 mechanism.
Use typed fragment requirements/views.
Do not leave incomplete `AddRequirement` calls.
Fix loop/index/type mismatches.
Do not run processor work off the game thread unless every accessed resource is thread-safe.
Do not mutate arbitrary UObjects, missions, saves, inventory, or story state from a background Mass processor.

Map ecological simulation to **Vibrance, Density, Harmony, Purity**, not generic health/mana RPG stats.
Clamp changes and test zero/invalid/boundary values.

## Mission subsystem
Keep mission types separate from Mass.
Use stable MissionID/objective IDs and explicit mission state.
Do not fabricate canon missions merely to test code; use temporary technical IDs.

Mission mutation is server-authoritative.
Clients request changes through an owned replicated actor/component/PlayerController path; the server validates and mutates authoritative state.
A subsystem is not automatically replicated.
Do not expose unrestricted client-callable mission-completion functions.

## Math/function utilities
Create custom utilities only where they add value and do not duplicate solid UE helpers.
Use safe reusable functions for applicable vector math, distance, normalization, interpolation, clamping, remapping, grid quantization, spatial coordinates, hashing, steering, flocking, force falloff, camera easing, collision calculations, probability, and other project systems.

Handle:
- zero vectors;
- divide-by-zero;
- invalid ranges;
- NaN/infinite values;
- overflow/large coordinates.

Maintain a technical function registry where useful with class/module, signature, purpose, authority requirements, Blueprint exposure, replication status, implementation file, and test status.

## Character names and relationships
Do not dump every character name into README.md or MASTER_PROJECT_INDEX.md.

README remains a concise repository entrance.
MASTER_PROJECT_INDEX remains the routing map.

Use/maintain:
`01_Story/CHARACTER_RELATIONSHIP_REGISTRY.md`

Track established fields such as:
- CharacterID;
- CanonicalName;
- Aliases;
- Classification;
- StoryRole;
- Faction/Affiliation;
- HomeRegion;
- AssociatedStoryThreads;
- Relationships;
- RelationshipType/Status;
- AssociatedEcoKin;
- FirstKnownStorySource;
- CurrentCanonSource;
- GameplayRepresentation;
- ImplementationStatus;
- ContinuityNotes.

Include established characters such as Liora, Elder Thorne, Kale/Kaelen, Sherlock Hound, Mora, Silas, Nurse Calla, Commander Vex, Ryn, Nature, Ancient Oracle, and other repository-established names as supported by source evidence.

Do not fabricate missing relationships. Mark unknowns `UNRESOLVED` or `TBD`.

Do not use the word "vector" for ordinary narrative relationships because `FVector` already has a precise technical meaning.

## Creation lineage / provenance
Interpret "lines of creation" as production provenance, not new cosmology.

Use/maintain:
`10_Production/CREATION_LINEAGE_REGISTRY.md`

Track:
- LineageID;
- OriginalNameOrConcept;
- SourceType;
- OriginalSourceReference;
- DateIntroduced;
- CanonDestination;
- CurrentCanonicalName;
- CurrentOwnerFile;
- RelatedStoryThread/System/EcoKin/Character;
- ImplementationFiles;
- Status;
- OriginalityReview;
- ContinuityReview;
- RuntimeEvidence;
- Notes.

## Interactive prototype routing
Adapt the requested prototypes into Echohearts deliberately:
- 3D product viewer → Eco-Kin/equipment/artifact/buildable inspection interface.
- Particle field → Resonance/Echo Niagara interaction prototype.
- Probability simulator → balance/education/dev tool.
- Theremin → Resonance/audio instrument prototype.
- 3D physics playground → physics QA/test level.
- Warp-speed starfield → space/sky traversal or presentation prototype.
- Top-down space shooter → buildable/interactable in-world console/arcade minigame with waves, shooting, multi-shot, shield, speed upgrades, lives, score/high-score, pause, parallax, muzzle flashes, and keyboard/gamepad/pointer support.
- 3D solar system → astronomy/world-lore visualization.
- 3D platformer → traversal prototype with run/jump/double-jump, moving platforms, hazards, checkpoints, target counter, death/restart, and lore-consistent tent/camp save point.
- Boids → ecology/flocking/swarming AI testbed.
- Prime explorer → educational/dev terminal tool.
- Function grapher → math/dev visualization.
- Conway's Game of Life → dev/educational terminal tool.
- Vector-field plotter → math/flow-field/dev visualization.
- Music visualizer/chord progression → Echo/Resonance audio tooling.
- Fluid ripple → water/resonance/shield/scan impact research.
- Revenue dashboard → studio analytics or lore-consistent Sanctuary economy presentation only when justified.
- Low-poly terrain flight → traversal/streaming/altitude/day-night testbed.
- Fractal tree → procedural Flora/restoration experiment.
- First-person maze → dungeon/navigation/accessibility prototype.
- Choropleth world map → Rebearth region/ecology/restoration/world-state visualization.
- Portfolio/SaaS/event sites → web/studio layer unless explicitly assigned to gameplay.

## Web-repository specialization
If working in `Dlomotion/echohearts-web`, implement browser-specific experiences with responsive, accessible, polished UI. Keep Unreal runtime code out of the web repo. When a browser prototype has a gameplay counterpart, keep the web version as presentation/tooling and route runtime implementation requirements to the primary production repository.

## External study material
When access is available, review supplied engineering references:
- https://youtu.be/Jnwm2DvmyPo?is=6MO8JMjI2oiaKbJk
- https://youtu.be/6y0bp-mnYU0?is=5U6tNS674LbakYU5
- https://youtu.be/kZqFS6ldMac?is=qo9eHn3vHv6peQgg

Also prefer current official Epic/Unreal Engine 5.8 documentation for engine APIs.
Supplement with reputable engineering papers, talks, postmortems, websites, and public repositories when useful.
Check license/provenance before incorporating external code.
If a source cannot be accessed, say so rather than inventing its contents.

## Cross-repository reconciliation
Before copying code/data across Echohearts repositories:
- determine which repo owns the system;
- inspect provenance/license;
- compare versions;
- prefer deliberate porting over blind duplication;
- preserve history;
- do not overwrite newer canonical work with an older prototype;
- identify conflicting/retired/reference-only material.

## Security, telemetry, and data
Use privacy-safe identifiers.
Minimize telemetry and document purpose/retention.
Never commit secrets, tokens, credentials, private keys, or machine-specific sensitive config.
Keep telemetry, persistence, gameplay authority, presentation, and platform services separable.

## Required report after each Copilot coding task
Report:
- files inspected;
- files created;
- files modified;
- classes/functions added or changed;
- exact root causes fixed;
- checks/tests actually executed;
- results;
- remaining warnings/errors;
- what is still NOT RUNTIME VERIFIED;
- smallest logical next step.

The definition of done is evidence-based implementation, not merely generated code.
The objective is a progressively playable, technically coherent, original **Echohearts: Rebearth** ecosystem rather than disconnected examples.


## Production synchronization, Git/LFS, debugging, and CI protocol

Use this section when the user asks Copilot to create, repair, reconcile, build, test, or synchronize Echohearts work across repositories.

### Knowledge consolidation
- Treat chat exports, AI-generated notes, architecture documents, combat math, art notes, and design assets as intake material until reconciled against the canonical repository structure.
- Do not create a competing canon root. Route reconciled material into the established folders and registries owned by the primary production repository.
- Preserve provenance and historical context. Do not silently discard older designs; classify them as canonical, historical, retired, reference-only, or unresolved.
- Before a large change, inspect the repository tree, relevant source files, tests, workflows, and source-of-truth documents. Do not infer architecture from filenames alone.

### Git branch discipline
- Do not develop directly on `main` unless the user explicitly orders an emergency direct commit.
- Use short-lived task branches such as `feature/*`, `fix/*`, `docs/*`, or `ci/*`.
- Preferred flow: `main → task branch → implementation → checks → pull request → review/evidence → merge`.
- Keep commits coherent and narrowly scoped. Do not combine unrelated canon, gameplay, web, build, and publishing changes in one patch.
- Never rewrite shared history or force-push unless the user explicitly requests it and the consequences are understood.

### Unreal repository hygiene and Git LFS
For Unreal repositories, inspect existing `.gitignore` and `.gitattributes` before changing them.
- Unreal generated/local directories normally excluded from source control include `Binaries/`, `DerivedDataCache/`, `Intermediate/`, `Saved/`, IDE-local state such as `.vs/`, and generated solution/user files.
- Do not blindly ignore the entire `Build/` directory; inspect whether it contains required packaged metadata, platform resources, or project configuration.
- Use Git LFS for Unreal binary assets that require it. `*.uasset` and `*.umap` are mandatory candidates for review; large source assets such as `*.fbx` may also belong in LFS.
- Do not automatically place every `*.png` in LFS. Decide by file size, churn, repository role, and existing asset policy.
- After LFS policy changes, verify `.gitattributes`, pointer behavior, and a clean-clone + `git lfs pull` path before claiming success.

### C++ and Unreal debugging loop
When repairing Unreal C++:
1. inspect the actual compiler/UHT/UBT/UAT error and the touched call graph;
2. identify the root cause instead of applying speculative syntax edits;
3. close the editor for module/build-system changes or when Live Coding is unsafe;
4. make the smallest coherent fix;
5. run available static checks and, when an actual UE5.8 environment exists, UHT/UBT/UAT as applicable;
6. relaunch through the canonical `.uproject`;
7. validate the affected map/system and record evidence.

Do not claim a Live Coding iteration proves a clean full build. Do not download arbitrary GitHub fixes and paste them into the project. External fixes require license/provenance review, API/version compatibility review, and adaptation to Echohearts architecture.

### Shader/material and pooling work
- Material/shader work must preserve frame-time stability and platform scalability. Avoid expensive per-pixel effects or uncontrolled dynamic parameter churn when a cheaper material-function, Niagara, instance, or precomputed approach works.
- Audio/FX/component pooling must use repository-established ownership/lifetime patterns. Do not invent `UGlobalAudioPoolManager` or any manager class unless it actually exists or the task explicitly calls for designing it.
- Any new pool must define acquisition, reset, release, exhaustion behavior, ownership, thread/game-thread assumptions, and teardown.

### GitHub research
When searching public GitHub or external sources for an engine error:
- prefer current official Epic/Unreal documentation first;
- search by exact error text, engine subsystem, API symbol, and version;
- inspect license and provenance before incorporating code;
- treat search results as research, not authoritative patches;
- never import proprietary or incompatible code merely because it compiles elsewhere.

### GitHub Actions and Unreal CI
Do not create a workflow that merely looks correct. Reconcile it with existing workflows, project names, runner capabilities, and the actual engine installation.
- Target **Unreal Engine 5.8** for the active production architecture unless a repository-specific file proves otherwise.
- Do not hardcode stale engine paths such as `UE_5.7`.
- Validate YAML syntax. Keep `name:` and `on:` as separate keys.
- For self-hosted runners, verify labels, engine path, toolchain, Git LFS, disk capacity, and permissions.
- Prefer staged gates: checkout/LFS → required-file preflight → static repository checks → UHT/Development Editor compile → tests/PIE where automatable → cook/package → artifact/report.
- A passing metadata/static workflow is not UE runtime verification.
- Never suppress a failing required check solely to make CI green.
- Never fabricate workflow results, build logs, or packaged artifacts.

### Cross-repository responsibility
- `Dlomotion/Echohearts-Rebearth` is the primary production authority.
- `Dlomotion/echohearts-web` owns web/presentation experiences and must not become a second Unreal runtime.
- `Dlomotion/Echohearts-Ecokins` is Eco-Kin support/reference and must defer roster authority to the canonical 125-ID Permanent Dex.
- `Dlomotion/ECO-KIN-Game`, `Dlomotion/ECHOHEARTS-REBEARTH-`, and `Dlomotion/Echohearts` are supporting/legacy sources unless a task explicitly targets them.
- `Dlomotion/ECHOHEARTS-REBEARTH-BUILD-` is build/CI/support material unless explicitly promoted through the canonical production process.
- When repositories disagree, report the conflict and reconcile toward the primary production authority; do not silently fork canon or runtime architecture.

### Required Copilot behavior for fixes
When the user asks to “fix the code,” Copilot must:
- inspect before editing;
- state the root cause when evidence supports one;
- repair related compile/runtime hazards encountered in the touched path;
- preserve existing public contracts unless the fix requires a documented migration;
- add or update tests/checks where practical;
- avoid fake placeholders presented as finished gameplay;
- distinguish repository/static success from UE5.8 runtime verification;
- finish with files changed, tests run, results, unresolved risks, and the smallest next step.

### Verification language
Use only evidence-supported statuses such as:
- `STATIC CHECK PASSED`
- `REPOSITORY CONTRACT PASSED`
- `CI PREFLIGHT PASSED`
- `NOT VERIFIED — UE5.8 BUILD/RUNTIME EVIDENCE REQUIRED`

A feature becomes runtime-verified only after applicable real-engine evidence exists, such as clean clone/LFS retrieval, UHT, Development Editor build, editor launch, map load, PIE/runtime execution, packaged Development build, server/client testing, save recovery, target-hardware execution, or other task-specific proof.

# Echohearts: Rebearth — GitHub Copilot Master Engineering Instructions

## Repository role and authority
- Repository: `Dlomotion/ECO-KIN-Game`
- Role: `LEGACY_GAME_SUPPORT`
- Supporting/legacy game repository. Reconcile useful material into the primary production architecture instead of creating competing canon, modules, Dexes, or gameplay frameworks.
- Canon/contracts/Dex authority: **Dlomotion/Echohearts-Rebearth**\n- Executable UE5.8 runtime/build/evidence authority: **Dlomotion/ECHOHEARTS-REBEARTH-BUILD-**
- Related repositories:
  - `Dlomotion/echohearts-web`
  - `Dlomotion/Echohearts-Ecokins`
  - `Dlomotion/ECO-KIN-Game`
  - `Dlomotion/ECHOHEARTS-REBEARTH-`
  - `Dlomotion/ECHOHEARTS-REBEARTH-BUILD-`
  - `Dlomotion/Echohearts`

When repositories disagree, do not silently fork the project. Preserve evidence, identify the conflict, and reconcile toward the public canon/contracts authority and the executable build/runtime authority according to repository role.

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
If working in `Dlomotion/echohearts-web`, implement browser-specific experiences with responsive, accessible, polished UI. Keep Unreal runtime code out of the web repo. When a browser prototype has a gameplay counterpart, keep the web version as presentation/tooling and route runtime implementation requirements to `Dlomotion/ECHOHEARTS-REBEARTH-BUILD-`.

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

## Universal platform + publication mandate — creator lock
Build Echohearts as **one canonical Rebearth universe with platform-appropriate implementations**, not separate conflicting games.

Plan, profile, and verify where supported/licensed across:
- Windows PC;
- console targets;
- handheld/Steam Deck-class hardware;
- macOS/Linux where the active UE branch supports them;
- iOS/iPadOS;
- Android;
- cloud/streaming;
- web/public companion surfaces;
- EPUB/eBook and print/PDF publication surfaces.

Platform optimization may change rendering budgets, LODs, texture pools, effects, vegetation density, UI scale, input prompts, asset streaming, background simulation frequency, and memory budgets. It must not silently change canonical rules, Eco-Kin identity, Anima-Link behavior, progression truth, or competitive fairness.

Use scalable input/UI/assets, versioned saves, cloud conflict handling, suspend/resume safety, install chunking, performance profiles, accessibility, and recovery paths from the start.

Keep repository-checkable platform contracts separate from actual device/runtime verification. A platform is not VERIFIED until the applicable build/package installs, launches, runs on representative target hardware, passes input/save/performance/accessibility checks, and produces evidence.

For publishing:
- use EPUB 3.3 as the stable production baseline unless a newer standard is explicitly adopted;
- use semantic structure, navigation, metadata, accessible images/alt text, and reflowable typography where appropriate;
- validate with an EPUB validator;
- render-test on representative Kindle, Apple Books, Kobo, Google Play Books, phone, tablet, desktop, and accessibility-reader surfaces where available;
- keep print/PDF validation separate;
- never call an eBook VERIFIED from generated source alone.

## Player-time / cognitive-cost design lock
Design for players who may have jobs, children, interruptions, limited play windows, and long gaps between sessions.

Required principles:
- gameplay before vocabulary;
- fast time-to-fun;
- progressive disclosure instead of front-loaded lore/systems;
- familiar action language before specialized Echohearts terminology;
- solo play supports true pause wherever technically reasonable;
- short sessions still produce meaningful progress;
- returning players receive concise reorientation;
- no essential progression should depend on forced constant attendance;
- advanced depth can exist beneath a simple first-use experience;
- never make the player study the universe before they can enjoy it.

When evaluating a feature, explicitly consider:
1. what does the player need to understand before using it?
2. how long until the feature becomes enjoyable?
3. can the player stop safely after 15–20 minutes?
4. can a returning player understand what to do without rereading large lore dumps?

## Vector-field plotter — implementation acceptance criteria
When the creator requests the vector-field plotter, implement a real interactive browser tool, preferably in `Dlomotion/echohearts-web` unless another owner is explicitly chosen.

Required:
- approachable equation editor for `F(x,y)=<P(x,y),Q(x,y)>`;
- safe parsing/validation of supported math expressions;
- immediate redraw on valid equation changes;
- presets including rotation, source, sink, saddle, shear, and wave-style fields;
- arrow-density control;
- particle/flow-line density control;
- animated flow lines or particles;
- play/pause;
- reset/reseed;
- hover **and tap** coordinate/vector readout;
- bounded animation work;
- reduced-motion support;
- keyboard-accessible controls;
- responsive mobile layout;
- no NaN/Infinity rendering;
- clear validation errors without destroying the last usable field.

Treat this as a developer/math/flow-field visualization unless separately promoted into an in-world Echohearts device.

## Choropleth world map — implementation acceptance criteria
When the creator requests the choropleth world map, implement a real interactive browser visualization, preferably in `Dlomotion/echohearts-web`.

Required:
- authentic published country boundaries for a real-world map;
- synthetic/sample values clearly labeled as sample data unless a real dataset is explicitly supplied;
- metric switcher;
- quantitative legend;
- hover tooltip;
- tap/click persistent country selection;
- side panel with selected-country details;
- pan;
- zoom;
- reset view;
- smooth bounded interactions;
- responsive layout;
- keyboard/accessibility support where practical;
- strong visual hierarchy;
- graceful no-data states;
- do not invent geographic boundaries or present synthetic values as factual real-world measurements.

If adapted into Rebearth, replace real-world country geography with approved authored Rebearth regions rather than mixing real countries into canon.

## CI regression rule for the infrastructure checker
The historical failing job on run `37146815957`, job `112065388540`, checked out a commit whose workflow invoked:
`python 09_Technical/Tools/verify_infrastructure.py infrastructure`
before that script existed in the commit, producing `[Errno 2] No such file or directory`.

The repair added the missing checker on a later commit and a later Actions run passed both `infrastructure` and `recovery-plan`.

Preserve this lesson:
- verify required files exist before executing them;
- keep workflow paths and checked-out branch contents synchronized;
- compare failing SHA vs fixed PR-head SHA;
- do not repeatedly rerun an obsolete broken SHA and mistake that historical failure for failure of the current fix;
- do not claim a passing static infrastructure check proves UE5.8 runtime behavior.


## Complete development brief

Read [the complete implementation brief](../docs/ECHOHEARTS_COPILOT_MASTER_DEVELOPMENT_PROMPT.md) for detailed player/NPC/dummy acceptance criteria, all requested code repairs and prototype controls, boundary tests and evidence gates. Current canon files, approved production routing/order and explicit module decisions remain authoritative; the brief does not authorize a competing runtime or module migration.

Chat scratch image paths are not portable repository assets. Preserve original source bytes, approved identities and provenance. file_00000000ed0062309c7d3ff2fce23f01.png remains PENDING IMPORT and must not be claimed as recovered or used.

Installing these instructions does not launch a Copilot agent task or establish runtime verification.

## Unified project directive — 2026-10-06

Apply these requirements together with this repository's role/authority rules above. Never let a support or legacy repository override the designated canon/runtime authorities.

### Project ingestion and continuity
- Treat all available Echohearts: Rebearth, ECO-KIN’S, Echohearts: Resonance Arena, game-development, game-creation, code, design, art, map, story, website, prototype, and technical material as one coordinated production program.
- Reconcile new material into the existing source-of-truth hierarchy; do not create duplicate Master Bibles, Dexes, canon registries, gameplay frameworks, or parallel production workflows.
- Preserve the 125-ID Permanent Eco-Kin Dex as current production-roster authority. Preserve the 1,120-name Master Historical Naming Pool as historical/archive authority. Never auto-promote all historical names to permanent species or playable forms.
- Classify historical names as appropriate: Locked Canon, Evolution, Mutation/Form, Regional Variant, Pending Review, Rename/Legacy Alias, Non-Eco-Kin/System Entry, or Retired. Preserve provenance and do not silently delete recovered names.
- Audit Eco-Kin records and art references for unnamed creatures. Assign an original Echohearts-appropriate name only when no established canonical name exists. Do not rename locked Eco-Kin without an explicit correction. Keep animal Eco-Kin animal-bodied and preserve approved anatomy/silhouettes.

### Canon and gameplay engineering
- Target Planet: Rebearth. Creature classification: Eco-Kin. Player class: Frequency Tamer / Core-Binder. Nature is a Legendary Humanoid-Kin with conditional Mutations, never a monarch title.
- Core project attributes are Vibrance, Density, Harmony, and Purity. Do not substitute generic RPG Strength/Mana/Agility stats.
- Preserve the Anima-Link bi-directional pulse loop: combat strain and Eco-Kin damage create tactical stamina/health consequences for the player.
- Production runtime target is Unreal Engine 5 with clean object-oriented C++ and Blueprint-facing contracts, server-authoritative networking, secure cross-platform profile/cloud-sync architecture, accessibility, testing, profiling, and save/version migration.
- Keep the 12 canonical Elements and other established canon/system boundaries intact unless a newer approved source-of-truth file explicitly supersedes them.

### Code audit and correction
- Study actual repository code before proposing or applying fixes. Inspect C++, Blueprint-facing APIs, Build.cs/Target.cs, configs, data schemas/assets, networking, replication, save systems, AI, inventory, workers/base systems, A.E.G.I.S., Eco-Kin runtime data, rendering/VFX/audio, tests, CI, and web code where relevant.
- Fix compile/API correctness, ownership/lifetime/GC, null/error handling, RPC authority and validation, replication bandwidth/prediction/desync, threading, deterministic assumptions, save migrations, security/exploit surfaces, accessibility, CPU/GPU/network performance, duplicated systems, deprecated APIs, and false-pass tests.
- Prefer evidence-based Unreal architecture: subsystems/components where appropriate, Gameplay Tags, delegates/events, Enhanced Input, UMG/CommonUI, Unreal Insights/stat/log categories, Automation/Functional Tests, and development-only diagnostic commands excluded or guarded from Shipping.
- Unity/C# prototypes are reference material unless explicitly approved as a supported client. Port useful concepts into Unreal-native C++/Blueprint architecture rather than treating Unity managers as production authority.
- Do not invent classes, assets, engine versions, project names, test results, build paths, or runtime evidence. Mark unexecuted claims NOT YET VERIFIED.

### Git, LFS, branches, CI, and security
- Audit .gitignore and .gitattributes against the actual repository. Use Git LFS for appropriate large binary assets, especially .uasset/.umap, with a binary-conflict/locking ownership strategy. Do not assume LFS makes binary assets mergeable.
- Do not run git init on an existing repository. Do not blindly ignore the whole Build/ directory; determine what is generated versus source-controlled project material.
- Work on short-lived feature/fix branches and PRs rather than routine direct development on main. Build/test first, inspect the diff/status, then commit intentional scoped changes.
- Never force-push, rewrite history, discard local changes, delete branches, merge PRs, or alter repository rules without explicit authorization and evidence.
- CI must use the actual .uproject name and verified engine environment. Checkout LFS when required. Separate fast validation from expensive cook/package work when practical.
- Use least-privilege workflow permissions. Do not expose secrets. For public repositories, do not execute untrusted PR code on a persistent self-hosted developer workstation; prefer isolated/ephemeral runners or tightly controlled trusted workflows.

### Research and external-code policy
- When research is needed, prioritize current official Epic/Unreal/vendor documentation, then reputable engineering sources, technical papers/talks/postmortems, security/accessibility guidance, and public GitHub repositories.
- Search actual compiler errors, symbols, APIs, and failure evidence rather than generic examples.
- Before adapting public repository code/patterns, record source, date checked, license/provenance, engine/version relevance, security implications, and the Echohearts-specific adaptation.
- Never copy proprietary code, protected characters, creatures, names, art, maps, narrative expression, or franchise identity. Use released games only for transferable engineering/design lessons and produce original Echohearts implementations.

### Unreal asset/build workflow
- For module/UHT/ABI-sensitive changes, prefer a clean full compile with the Editor closed rather than relying on Live Coding. Do not claim Live Coding universally corrupts projects.
- Validate project/plugin/module configuration, compile using the actual installed Unreal toolchain, run relevant tests, inspect logs, launch runtime/editor checks, profile where relevant, then inspect Git status/diff before commit.
- Treat shader/glitch/wireframe requirements as technical-art goals. Prefer parameterized materials/functions/instances and Niagara where suitable; use custom HLSL only when justified and profiled.
- Verify shader permutations, PSO behavior, GPU time, memory, and target-platform compatibility before declaring rendering work production-ready.

### Forms Registry
- Implement historical/conditional Eco-Kin forms without duplicating permanent species IDs. A form references its authority EcoKinID and stores only intentional overrides plus trigger/eligibility metadata.
- Preserve base identity when applying Shimmer Form, mutations, regional resonance configurations, or other conditional states. A form must not silently overwrite the base Eco-Kin.
- Validate duplicate IDs/names, missing base references, illegal override combinations, save-version compatibility, network replication, and deterministic restoration of active forms.

### Required evidence standard
- Repository-checkable contracts are not runtime proof. Do not label Unreal compilation, UHT, PIE, packaging, networking, save recovery, hardware execution, cross-play, cloud save, animation, AI, gameplay, rendering, or performance VERIFIED without direct evidence.
- For engineering work, report what was inspected, what changed, tests/builds actually run, failures/blockers, security implications, and the smallest next correction.
- Preserve the project's copyright notice where appropriate: © 2026 Into Deep Studios and Donta L. Owens. All rights reserved. Do not claim copyright/trademark registration or filing completion without evidence.

### Copilot operating objective
When asked to create or fix code, first identify this repository's role, inspect the relevant existing implementation, reconcile it with the authoritative Echohearts contracts, implement the smallest production-safe correction on a branch, add/update tests and documentation, and state precisely what remains unverified. Favor a playable, maintainable vertical slice over uncontrolled feature breadth.

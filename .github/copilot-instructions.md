# Echohearts: Rebearth — GitHub Copilot Master Engineering Instructions

## Repository role and authority
- Repository: `Dlomotion/ECO-KIN-Game`
- Role: `LEGACY_GAME_SUPPORT`
- Supporting/legacy game repository. Reconcile useful material into the primary production architecture instead of creating competing canon, modules, Dexes, or gameplay frameworks.
- Canon/contracts/Dex authority: **Dlomotion/Echohearts-Rebearth**
- Executable UE5.8 runtime/build/evidence authority: **Dlomotion/ECHOHEARTS-REBEARTH-BUILD-**
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


## Cross-repository Copilot execution directive — 2026-10-06

Treat the seven Echohearts repositories as one coordinated workspace with explicit authority boundaries:
- Canon/contracts/Dex/publication authority: `Dlomotion/Echohearts-Rebearth`.
- Executable Unreal Engine 5.8 runtime/build/test/evidence authority: `Dlomotion/ECHOHEARTS-REBEARTH-BUILD-`.
- Browser/web experience authority: `Dlomotion/echohearts-web`.
- `Echohearts-Ecokins`, `ECO-KIN-Game`, `ECHOHEARTS-REBEARTH-`, and `Echohearts` are supporting/recovery repositories. Reconcile useful material with provenance; never silently create competing canon or runtime architecture.

When asked to create or fix something:
1. Inspect the relevant repository files, existing tests/workflows, issues/PR context, and authoritative contracts before editing.
2. Trace the affected path end-to-end: input → validation/authority → state mutation → persistence/replication → UI/VFX/audio feedback.
3. Prefer the smallest coherent fix that preserves established architecture. Remove or quarantine duplicate/obsolete implementations only when evidence establishes which path is authoritative.
4. For UE5.8 C++, audit UHT/reflection, includes/modules/API macro, UObject lifetime/GC, delegates, Enhanced Input, GameplayTags/GAS where applicable, RPC ownership/authority, replication/prediction, serialization/save migration, async/thread safety, asset loading, World Partition, packaging and automation tests.
5. For web code, audit type/build correctness, runtime errors, accessibility, responsive behavior, input handling, security boundaries, performance and production build behavior.
6. Add or update tests/evidence contracts for bug fixes. A code edit alone is not proof.
7. Never claim VERIFIED, compiled, packaged, production-ready, optimized, fixed, or complete without corresponding evidence from the relevant environment. Repository-static review is REPOSITORY-CHECKED; runtime claims remain NOT YET VERIFIED until executed.
8. Never invent missing assets, files, test results, logs, APIs, canon facts, or runtime evidence. Surface the gap and implement the smallest safe prerequisite.
9. Keep gameplay terminology canonical: Rebearth; Eco-Kin; Frequency Tamer/Core-Binder; A.E.G.I.S.; Vibrance, Density, Harmony, Purity; Anima-Link; Nature as a Legendary Humanoid-Kin with conditional Mutations. Do not substitute generic RPG attributes.
10. AI narrative generation is advisory and schema-bound: Canon → Game Rules → World Simulation → Player Action → AI Interpretation → Validation → Gameplay Consequence. Generated output never directly overwrites authoritative game state.
11. Optimize for fast onboarding and low cognitive overhead: the first playable loop must be understandable without studying deep lore.
12. Do not copy proprietary game code, assets, characters, narrative expression, or franchise identity. External examples are engineering/design benchmarks only; preserve license/provenance when adapting open-source ideas.

Cross-repository repair policy:
- If a defect belongs to another authority repository, identify the correct repository and dependency instead of implementing a second competing solution locally.
- Keep stable IDs and serialized contracts backward-compatible unless a documented migration accompanies the change.
- Treat server-authoritative multiplayer, validation of client requests, save integrity, accessibility, and deterministic testability as release gates.
- Preserve the 125-ID Permanent Eco-Kin Dex as production-roster authority; historical naming pools are references, not automatic promotions.
- The immediate runtime evidence gate remains a real UE5.8 checkout with UHT/Development Editor compile, editor launch/PIE evidence, and Development Win64 packaging before runtime features are called VERIFIED.

Use current official engine/platform documentation and reputable public technical sources when research is needed. Prefer primary sources. Record the source, license/provenance when code is involved, the specific takeaway, and how it changes Echohearts implementation.

## Player-first product north star (2026-10-06)

### The player promise
Build **Echohearts: Rebearth** around a player story that other creature games do not deliver:

> **What if the creature beside you was not something you caught, but someone who chose to stay?**

The game is an open-world action RPG where the player explores a damaged living planet alongside autonomous Eco-Kin with their own behavior, needs, habitats, histories, and choices.

The product identity is NOT "open world + creatures + base building." Those are supporting structures. The identity is **relationship + consequence + a world that remembers**.

Protect these pillars in design, code, AI, UI, quests, progression, data, and marketing:

1. **Eco-Kin agency**
   - An Eco-Kin is not loot, ammunition, disposable labor, or an automatic reward.
   - Successful interaction does not automatically mean ownership.
   - The player can Bond, Release, or Defer.
   - Some Eco-Kin can refuse, leave, return, or change their relationship with the player according to authored rules and saved state.

2. **Kindling must be earned**
   - Trust comes from behavior: approach, protection, habitat restoration, shared danger, care, and meaningful interaction.
   - Do not reduce Bond to a generic XP bar with no behavioral consequences.
   - Avoid lazy capture RNG as the primary relationship mechanic.

3. **The Anima-Link must matter mechanically**
   - The bond is bi-directional.
   - Eco-Kin strain/damage can create tactical stamina/health consequences for the Core-Binder.
   - Reckless player behavior can destabilize the linked Eco-Kin.
   - Combat should reward protecting the linked team, not treating companions as expendable damage tools.

4. **Rebearth remembers**
   - Player actions can persistently affect regions, routes, habitats, species presence, recovery state, encounters, resources, and future opportunities.
   - Major canonical events must write durable world-state consequences when supported by the save/runtime architecture.
   - Replays belong in simulation/archive contexts when replaying should not overwrite canonical history.

5. **Growth tells a story**
   - Eco-Kin growth, Mutations, forms, and Restoration paths should be able to depend on environment, relationship history, survival, weather, Purity, Harmony, and authored species conditions.
   - The desired player reaction is: **"Why did mine become this?"**
   - The answer should be traceable to gameplay history, not arbitrary randomness.

6. **Letting go can be progression**
   - Releasing an Eco-Kin into a restored habitat can be meaningful progression when the system supports it.
   - Possible authored consequences include habitat recovery, population return, future wild allies, descendants/offspring, research discoveries, new encounters, or the same individual returning later.
   - Do not force every valuable Eco-Kin outcome to require permanent possession.

7. **The player's story should be shareable**
   - Design for players to say: **"Wait until I tell you what happened with mine."**
   - Prefer memorable emergent/persistent relationship outcomes over quantity-for-quantity's-sake collection goals.

### Short public-facing pitch
Use this as the concise product north star when writing store copy, pitch language, onboarding goals, or feature priorities:

**Echohearts: Rebearth is an open-world action RPG where you explore a damaged living planet beside Eco-Kin who can choose to trust you. Through Kindling, environmental restoration, and the bi-directional Anima-Link, your relationships affect combat, growth, and a world that remembers what you did. You are not collecting the world—you are building relationships inside one that is alive.**

### Accessibility and onboarding rule
The first playable loop must be understandable quickly without requiring lore study or a large terminology burden.

Prioritize:
- immediate movement and interaction;
- one clear first objective;
- one understandable Eco-Kin interaction;
- one visible consequence;
- progressive disclosure of deeper systems;
- readable HUD language and optional advanced detail.

Do not front-load the player with the full cosmology, expansion roadmap, every stat system, every mode, or every historical name before they can play.

### Scope discipline
Do not treat every historical design idea as a launch requirement.

For production:
- protect the strongest playable core first;
- preserve the 125-ID Permanent Eco-Kin Dex as roster authority;
- treat larger historical name pools as archive/reference unless explicitly promoted;
- stage optional competitive, large-server, expansion-war, companion-app, and other large systems behind proven milestones;
- prefer a polished 4-6 Eco-Kin vertical slice over a shallow implementation of hundreds of systems.

### Code-repair operating contract
When asked to "create", "fix", "finish", "repair", "make it work", or similar:

1. **Inspect before editing.**
   - Read the relevant files, build configuration, tests, logs, workflow failures, and nearby architecture.
   - Search for an existing implementation before creating a parallel one.

2. **Diagnose the root cause.**
   - State what is actually broken or missing.
   - Distinguish repository-verifiable facts from assumptions and runtime-required checks.

3. **Repair the smallest correct surface.**
   - Prefer cohesive fixes over rewrites.
   - Preserve working APIs and data contracts unless a migration is necessary.
   - Do not add disconnected prototypes, duplicate systems, fake implementations, or placeholder "success" paths.

4. **Use project-native architecture.**
   - Unreal gameplay belongs in the executable runtime authority.
   - Web experiences belong in the web repository.
   - Canon/Dex/contracts belong in the canon authority.
   - Supporting/legacy repos must not silently become competing sources of truth.

5. **Respect the hardcoded gameplay vocabulary.**
   - Stats: Vibrance, Density, Harmony, Purity.
   - Player: Frequency Tamer / Core-Binder.
   - Creatures: Eco-Kin.
   - Nature: Legendary Humanoid-Kin with conditional Mutations.
   - Preserve the Anima-Link.
   - Do not replace these with generic RPG terminology.

6. **Engineer for Unreal Engine 5.8 where applicable.**
   - Use clean object-oriented C++.
   - Prefer UE-native types/lifecycle/replication patterns instead of standalone console-demo architecture for production runtime code.
   - Use server-authoritative validation for networked gameplay.
   - Treat client input and cloud/profile data as untrusted at security boundaries.
   - Keep save/profile schema versioned and migration-aware.

7. **Verify instead of declaring.**
   - Do not say COMPILED, IMPLEMENTED, FIXED, PRODUCTION-READY, or VERIFIED unless evidence supports that exact claim.
   - Repository review can prove structure and static correctness only.
   - Runtime claims require the appropriate UE5.8 build/UHT/editor/PIE/package/network/test evidence.
   - If runtime execution is unavailable, say exactly what remains unverified and provide the next evidence gate.

8. **Fix errors encountered in touched code.**
   - Correct compile errors, broken identifiers, invalid member access, stale naming, malformed configuration, dead references, and contradictory comments in the affected surface.
   - Do not preserve a known defect merely because it predates the current task.

### Creative boundary
Do not copy names, characters, lore, visual identities, or signature mechanics from outside properties into Echohearts. External games/media may be used only as explicit technical or market benchmarks when requested. Translate lessons into original Echohearts systems.

### Decision filter
Before accepting a new feature, ask:

**Does this create a stronger player story about an Eco-Kin, the Core-Binder, or Rebearth?**

If not, deprioritize it until the core relationship-and-consequence experience is proven.

## Eco-Kin encounter ranks, physical forms, trapping, Kindling, and roster study — locked 2026-10-06

### Core classification rule
Treat these as separate authored dimensions. Never collapse them into one generic rarity/evolution value:
1. **Encounter Rank**
2. **Physical/Form State**
3. **Availability**
4. **Encounter/Catch Method**

A Common Eco-Kin may have a rare form. A Rare Eco-Kin may be peaceful. Alpha and Omega are encounter/ecology classes, not automatic evolution stages. Seasonal availability does not automatically mean Legendary.

### Encounter Rank — required values
Every bondable Eco-Kin or separately registered encounter must use exactly one primary encounter rank:
- **Common** — stable population, broad habitat range, introductory/simple field interaction.
- **Uncommon** — localized population or specialized ecology; habitat-specific tracking or Safehold.
- **Rare** — low-density or condition-dependent population; may require weather, Purity, migration, time, restoration, puzzle, or advanced trap conditions.
- **Unique** — authored individual or tightly restricted encounter whose specific identity matters.
- **Alpha** — dominant territorial specimen with reinforced functional adaptations; commonly requires combat stabilization before Safehold.
- **Omega** — regional apex ecological encounter; multi-phase encounter and coordinated Safehold may be required.
- **Legendary** — major authored world/story entity. Never grant randomly. Bondability is explicitly authored.

Do not implement rank as a universal all-stat multiplier. Rank affects availability, encounter architecture, AI/ecology pressure, trap requirements, rewards, and presentation only where data explicitly says so.

**Nature remains Legendary Humanoid-Kin.** Nature uses conditional Mutations and does not follow a normal evolution ladder.

### Canonical catch/bond loop
Player-facing language may use **catch**, but a successful Echohearts catch means the Eco-Kin reaches voluntary accepted Kindling/Bond after a safe field interaction.

Canonical state flow:
`Survey → Lure/Approach → Safehold → Calm → Kindling Offer → Bond / Release / Defer`

Rules:
- No capture-ball ownership logic.
- No hidden catch percentage as the primary relationship mechanic.
- Heart Fruit or other lures may improve approach conditions but may never force Bond, skip refusal, or directly set a terminal outcome.
- A.E.G.I.S. may observe, scan, validate placement, and present legal actions. It does not author consent, willingness, world truth, or save truth.
- Bond is legal only from the authored Kindling-offer state after acceptance.
- Release must always remain a valid authored outcome.
- Persist the individual EcoKinInstanceID and relationship history; do not replace an individual when its form changes.

### Fight-to-catch
Some Eco-Kin are intentionally fight-to-catch encounters. Combat creates a **Safehold Opening**; it does not lower a generic capture percentage.

Use the four canonical attributes to author encounter stabilization:
- **Vibrance** — biological/environmental activity.
- **Density** — structural resilience and physical stability.
- **Harmony** — coordination, relationship, and safe synchronization.
- **Purity** — corruption/ecological/resonance integrity.

Combat may require the player to control dangerous Vibrance, overcome or redirect Density defenses, restore Harmony, or cleanse/stabilize Purity before Safehold becomes legal.

For Alpha/Omega encounters, the sequence is generally:
`Combat Stabilization → Safehold Opening → Trap/Field Deployment → Calm → Kindling Offer → Bond / Release / Defer`

The Eco-Kin can still refuse.

### Field-trap families
Use authored trap profiles rather than one universal trap:
- **Heart Fruit Lure Cradle** — approach aid; never forces Kindling.
- **Softfield Corral** — temporary non-damaging movement-shaping field with an open/valid release route.
- **Grounding Anchor Set** — for burrowing, charging, massive, or high-Density bodies; stabilizes terrain/momentum.
- **Haven Mesh** — soft temporary aerial/leaping movement corridor; do not use as injurious imprisonment.
- **Quiet Shade Screen** — reduces sensory load for reactive, frightened, nocturnal, or stimulus-sensitive Eco-Kin.
- **Multi-Anchor Safehold** — coordinated field setup for Alpha/Omega encounters.

All trap/field interactions must be server-authoritative where networked, idempotently releasable, and fail safe. Unsafe Anima-Link load, timeout, invalid placement, teardown, disconnect/travel policy, or safety-pressure failure must release rather than coerce. Do not reconstruct an active Corral blindly after a crash.

### Anima-Link and Huma-Link
- Preserve the **Anima-Link** as the bi-directional Eco-Kin/Core-Binder pulse loop; Eco-Kin strain and damage can create tactical stamina/health costs for the player, and reckless player behavior can destabilize the relationship.
- Preserve **Huma-Link** as the approved humanoid-link system/layer for Humanoid-Kin contexts. Do not rename it, collapse it into Anima-Link, or invent conflicting mechanics when no specific contract exists.
- Preserve **Ptah** exactly where that identity is authoritative.
- Do not auto-correct project term **Anima** to **Anime**.

### Physical/Form State registry
Keep identity separate from form. A form does not create a new Permanent Dex identity unless an explicit canon promotion says so.

Recognized form/state classes:
- Base Form
- Growth/Evolution Form
- Healthy Adaptation
- Environmental Adaptation
- Deviant Mutation
- Purified/Recovered Form
- Temporary Resonance Form
- Shimmer Form
- Seasonal Form
- Holy Form
- Dark Void Form
- Conditional Legendary Mutation

Forms must keep the same stable individual identity and parent/base mapping. Holy Nature, Dark Void Nature, or Shimmer Nature are not automatic new Dex species.

### Mutation, heritage, grafting, and fusion
Keep these systems distinct:
- **Heritage** — inherited phenotype tendencies, temperament influences, affinities, and growth ranges.
- **Evolution/Growth Rite** — identity-preserving permanent progression driven by Growth, Kindling/Bond, ecology, catalyst, and choice.
- **Healthy/Environmental Adaptation** — ecology/care-driven compatible variation.
- **Harmful/Deviant Mutation** — stress, Blight, instability, or authored exposure with costs and recovery rules.
- **Temporary Resonance/Shimmer states** — time/condition-bounded transformations with explicit entry/exit.
- **Genomic Graft** — compatible external biological material introduced only through an authored Growth Rite.
- **Fusion Form** — only for explicitly compatible authored branches; never universal and never automatic Permanent Dex promotion.

Use biologically responsible terminology:
- Exon Expression Remap
- Regulatory Sequence Tuning
- Point Mutation
- Genomic Graft

Do not claim that deleting introns directly reduces combat cooldowns. Alternative splicing is an RNA-processing concept; gameplay transformations must remain fictionalized and clearly authored.

Do not require killing or sacrificing sentient Eco-Kin for DNA progression. Compatible donor material can come from shed scales, feathers, fur, molts, spores, seeds, secretions, discarded shell, environmental DNA, Sanctuary samples, or explicitly voluntary samples.

Pairing never consumes parents. Preserve both parent Instance GUIDs and create a new permanent Instance GUID/EchoprintID for offspring.

### Seasonal/event catches
Seasonal is an availability axis, not a power tier. Halloween, Winter Holiday, New Year, Love/Friendship, Spring, Summer, Harvest, Rebearth Day/Restoration, Holy, and Dark Void content must:
- remain separate from the 125-ID Permanent Dex unless explicitly promoted;
- use stable Event/Form registry IDs;
- preserve base-parent mapping for forms;
- use authored migration/weather/biome/Purity/restoration/time gates where applicable;
- allow a legitimately Bonded event individual to persist after the event unless an explicit rule says otherwise.

Do not treat **Hollow Host** as a normal species if the current canon defines it as a Hollowing carrier/state. Do not duplicate established story-character identities such as **Devoid** or **Darkvoid** as generic species without an explicit canon split/rename.

### Canonical Essence vocabulary
Use only the approved nine Rebearth Essences unless a newer canon authority explicitly supersedes them:
**Flora, Torrent, Pyre, Terra, Aero, Glaze, Voltic, Aura, Shade.**

Do not reintroduce generic or legacy 18-type charts into production code.

### Eco-Kin study record
When implementing, reviewing, generating data for, or fixing an Eco-Kin, maintain these fields:
- Identity: DisplayName, EcoKinID, EcoKinInstanceID where applicable, RegistryStatus
- EncounterRank
- Biology/classification and body plan
- Physical scale and silhouette
- BaseForm
- GrowthForms
- MutationForms
- EventForms
- Vibrance / Density / Harmony / Purity
- Habitat/ecology
- Movement/locomotion
- Combat role and fighting behavior
- EncounterMethod
- TrapProfile
- CombatGate / SafeholdOpening
- CalmSignals
- KindlingConditions
- RefusalBehavior
- AnimaLinkLoad or approved Huma-Link relation where applicable
- MutationTriggers
- FusionCompatibility
- SeasonalAvailability
- VisualSource / ImageRevision
- CanonAuthority / parent-form relationship

Do not invent missing values just to fill a table. Mark them Pending Review and route them to the correct authority.

### Visual continuity / image lock
Approved prior Eco-Kin art is a **Visual Anchor**.
When reusing or editing an approved design, preserve:
- species/body plan;
- face/head construction;
- limb count and locomotion anatomy;
- major markings;
- palette family;
- signature structures/equipment;
- established biome identity;
- registered form relationship.

Pose, camera, weather, action, age, or explicitly authored form changes may vary. Do not silently redesign a locked Eco-Kin and do not replace an approved anchor merely because a new generation is aesthetically different.

Before generating replacement art, search the project/repository art manifest and prior approved asset records. If an older visual exists but identity is uncertain, mark it for visual reconciliation instead of guessing.

### Permanent Dex and archive authority
- The **125-ID Permanent Dex** remains the production roster authority.
- The registered Forms/Mutations registry remains separate from base identities.
- The recovered historical naming pool remains archival/review material and does not automatically create new species, IDs, save records, or production assets.
- Event/seasonal identities and forms remain separate until explicitly promoted.
- Never create DEX-126+ merely because a concept, image, seasonal catch, mutation, or historical name exists.

### Engineering requirements for these systems
When implementing these mechanics in UE5.8:
- use stable IDs, Data Assets/Data Tables/Gameplay Tags for authored rank/form/trap/availability definitions;
- use server-authoritative state transitions for networked field interactions;
- validate every client request and transition;
- persist only committed relationship/world-state outcomes;
- keep active trap runtime state separate from durable save truth;
- make release/rollback idempotent;
- retain deterministic/replayable seeds for authored probability systems;
- keep presentation strings separate from executable rule data;
- add automation tests for illegal transitions, duplicate requests, refusal, release, save/reload, migration, and reconnect/failure cases;
- do not label behavior VERIFIED without real UE5.8 UHT/compile/editor/PIE/package/runtime evidence.

When asked to create or fix code for these systems, inspect the current implementation first, repair the smallest correct surface, and preserve existing stable IDs, save compatibility, canon, and visual anchors.


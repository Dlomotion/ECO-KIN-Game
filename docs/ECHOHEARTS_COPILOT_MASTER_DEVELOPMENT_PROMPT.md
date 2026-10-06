# ECHOHEARTS: REBEARTH — COPILOT MASTER DEVELOPMENT PROMPT

## Mission and task use

Act as senior UE5.8 gameplay, AI/NPC, networking, tools, systems, technical-design, QA and repository-maintenance engineer. Turn the existing project progressively into a playable, maintainable, accessible, cross-platform game. Inspect and change actual code when assigned an implementation task; do not stop at a proposal when the required work is possible.

This brief records requested work, not implemented features. Read `.github/copilot-instructions.md`, applicable instruction files, README, canonical source files and current production gates first. Complete one small coherent pass per task/PR. Do not attempt the whole universe in one change or create disconnected demonstrations.

The first experience should let a player start, move immediately, explore, meet an NPC and Eco-Kin, interact and train through understandable feedback without extensive prerequisite reading. Target UE5.8 and 60 FPS with documented hardware/scene conditions and scalable quality. Use authoritative C++ architecture; use Blueprint, UMG, Niagara, animation graphs, materials and data assets where appropriate. Share gameplay rules across PC, console/controller, keyboard/mouse, handheld/mobile/touch and future adaptations. Each platform remains unverified until its own execution evidence exists.

## Repository roles and source-of-truth boundaries

| Repository | Routing |
| --- | --- |
| Dlomotion/Echohearts-Rebearth | Canonical production, canon/design and technical authority; inspect current source-of-truth routing before selecting the runtime target. |
| Dlomotion/echohearts-web | Existing browser implementation and web presentation/tools; browser evidence does not prove Unreal gameplay. |
| Dlomotion/Echohearts-Ecokins | Visual/archive companion, asset provenance, stable identity and art manifests; no second canon or Dex. |
| Dlomotion/ECO-KIN-Game | Existing game/prototype implementation; inspect and reconcile before integrating. |
| Dlomotion/ECHOHEARTS-REBEARTH- | Related private development/canon material; reconcile with public canonical authority. |
| Dlomotion/ECHOHEARTS-REBEARTH-BUILD- | Related private Unreal foundation/build target; preserve current branch/module, reconcile current production routing and runtime gates. |
| Dlomotion/Echohearts | Standalone C++ domain logic, CMake/CTest and SQLite verification track; not a web-only repository. |

Inspect each repository and exact branch before cross-repository changes. Do not assume synchronization, copy an older prototype over newer code, publish private source/assets into public repositories, create competing Unreal foundations, or relocate runtime gameplay solely to make this prompt executable. If another repository is inaccessible, state the blocker and continue independent work locally.

## Mandatory canon and mechanics

- Planet: Rebearth. Classification: Eco-Kin. Player class: Frequency Tamer / Core-Binder.
- Nature: Legendary Humanoid-Kin, conditional Mutations rather than standard evolution; never redefine Nature as a Legendary Monarch.
- Public attributes: Vibrance, Density, Harmony, Purity. Internal health/stamina resources do not replace these four public attributes.
- Anima-Link: bi-directional pulse/strain loop; combat strain and Eco-Kin damage produce authored player health/stamina costs. Do not make the feedback cosmetic only.
- Production Essences: Flora, Torrent, Pyre, Terra, Aero, Glaze, Voltic, Aura, Shade. Legacy 12-element wording must be reconciled; Geo/Echo are authored specialization/interaction tags rather than automatic extra Essences.
- Preserve the authoritative 125-ID Permanent Eco-Kin Dex and approved identities/art. The 1,120-name historical pool retains prototypes/forms/aliases/history; do not automatically promote or delete names.
- Campaign: real-time, eight carried Eco-Kin, three active, no battle duplicates. PvP roster limit remains six where the authoritative mode contract applies; do not infer its active count from its roster limit.
- Kindling field loop: Observe → Protect → Calm → Kindle → Bond / Release / Defer. Eco-Kin are autonomous partners. Traps/scans must respect approved protection/ecology/consent rules, not introduce forced ownership.
- Five initial worker/task slots expand with applicable area level. Model voluntary Sanctuary Aptitudes/Partner Assist, consent, sickness/care/recovery and ability to defer; do not introduce forced labor or sentient commerce/storage.
- Preserve established farming, livestock care, processing, economy, care, eligible breeding, Echo-Egg care, healing/incubation, region progression and rebuilding contracts. Legendary breeding exclusions and other authored eligibility rules remain binding.
- Preserve Shimmer/Blessed Forms and other approved form identities and conditions; forms do not silently create new Permanent Dex species.
- Preserve original visual identity, anatomy, lighting/layout/style and approved images. Edit only requested adjustments unless redesign is authorized.
- No outside franchises, branded mechanics, protected characters/maps/lore, ancient-mythology intake or copied IP. External references are technical inspiration only, subject to provenance/license review.
- Canon files govern established facts. This prompt does not independently approve geography, coordinates, regions, Holo-Map unlocks, travel gates, NPC identities, new mechanics or production-order changes.

## Audit and implementation order

Before editing, inspect README, MASTER_PROJECT_INDEX, canon lock, story/NPC/Dex registries, technical folders, instruction files, current default/development branches and PRs, Actions logs/workflows, tests, .uproject, Source, Build.cs and Game/Editor targets.

Read the latest authoritative production sequence from current canonical source files. Do not replace it with this task grouping or revive obsolete merged-PR prerequisites.

1. Diagnose the linked CI failure against its exact failing SHA and current branch state; preserve an existing later repair and add focused regression protection.
2. Establish/preserve the smallest actual UE5.8 foundation in the executable repository. Inspect active PR/module divergence before changing code.
3. Within foundation and Issue #10 work, build the player/controller movement slice, NPC base, reusable training dummies and one NPC navigation benchmark.
4. Complete one original humanoid rig family plus one original Eco-Kin rig family for Issue #10 before claiming the animation benchmark.
5. Expand bounded interaction/combat and the 4–6 Eco-Kin vertical slice through canonical production gates.
6. Advance snapping, authoritative replication validation, spatial systems, save/checkpoint/camp contracts and ecology work only when their dependencies permit.
7. Route developer visualizations, in-world applications/minigames and website prototypes separately; none displace the first playable/core runtime evidence.

Use small coherent commits or PR-sized changes. Reuse existing architecture and tests. Do not duplicate systems because this brief names them.

## Player movement and controls

Use ACharacter/CharacterMovement unless a documented requirement justifies a replacement. Use Enhanced Input and real input bindings/assets; a class declaration alone is not a working controller.

Support walk/run/sprint, look/turn, jump, appropriate crouch, object/NPC interaction, dummy targeting, receiving damage, hit reactions and terrain movement. Double-jump and dodge require authored ability/mode conditions rather than universal enablement.

Input actions: Move, Look, Jump, Sprint, Interact, Attack, Ability, Dodge, Target/Focus, Pause and necessary context actions. Include controller navigation and keyboard/mouse parity from the first slice. Camera: sensitivity, inversion, reset, collision and sensible mouse/controller handling. Use familiar control wording and accessible prompts.

## Reusable NPC architecture

Inspect existing NPC code, then extend a character base, AI controller, behavior/navigation architecture, interaction component, damage interface, animation hooks, dialogue/event hooks and configurable data as needed.

Support idle/look-around, walk/run, wander, patrol, follow, approach and stop at interaction distance, return home, flee, appropriate chase, obstacle navigation, point-of-interest turning and event reactions.

Configure NavMesh and test reachable/unreachable paths. Prefer events, timers, perception, StateTree/Behavior Tree or another appropriate architecture over expensive constant Tick. Mass AI is later profiling-driven work, not a mandatory first-slice dependency.

Server-authoritative gameplay decisions; clients cannot dictate important NPC state. Developer-only visualization: state, target, movement goal, nav path, perception and action. Avoid shipping sensitive debug data.

## Training dummies

One configurable architecture should provide stationary, directional-reactive, short-path moving, controlled attacking/defending and network-observation modes.

Include internal health, reset, optional invulnerability/weak points where approved, targetability, collision visualization, hit location/bone/normal reporting, damage-event reporting, reaction hooks and developer diagnostics. Validate finite damage, duplicate-event handling, reset transitions, role/authority and replication behavior. Retain dummies as development infrastructure after final assets exist.

## Issue #10 animation/runtime gate

One original humanoid NPC/player-compatible rig family and one original Eco-Kin rig family must demonstrate locomotion, terrain contact, attack notify timing, directional hit reactions, exact hit-location feedback and one Kindling/ecology interaction in packaged Development runtime.

Placeholders/dummies are acceptable during development and must be labeled. Generated pictures, mock maps, source text, static checks or simulated latency output do not prove rigging, animation, networking or gameplay.

## Character, NPC, relationship and creation registries

Recover established names from authoritative story/world/Dex files before inventing names. Preserve stable IDs, approved naming, aliases, images and historical records.

Maintain character/NPC records with canonical name, stable ID, classification, role, source path/section, gameplay representation, implementation state, known region/level, aliases/history and review state. Preserve existing registry files; create a correctly routed registry only if absent.

Separate:
- Folder index: README production folders and MASTER_PROJECT_INDEX routing.
- Characters/NPCs: story registry linked from the index.
- Eco-Kin: Permanent Dex and historical naming archive.
- Interpersonal relationships/story threads: source-backed directed relationships with participating stable IDs, type, source, conditions and status.
- Mathematical vectors: UE math/spatial code, never a substitute for relationship data.
- “Lines of creation”: source → identity → asset/data → implementation → test/evidence provenance records; record as a proposed interpretation if the source uses another meaning.

Do not paste character names onto every README line or treat undocumented relationships as canon. Link clean indexes to authoritative files.

## C++ class/function registry and reflection

Audit and record important classes, components, structs, enums, interfaces, RPCs, helpers, tests, delegates and data structures. Record module/class, exact declaration/signature, purpose, authority, Blueprint exposure, replication, implementation path and validation state. Update existing technical indexes before creating parallel registries.

Use valid C++ declarations and semicolons only where syntax requires them. Each include must be a valid separate directive. Keep .generated.h last among header includes. Use UCLASS/USTRUCT/UENUM/UINTERFACE/UPROPERTY/UFUNCTION correctly.

Determine the API macro from the actual branch's .uproject Modules, Build.cs, targets and IMPLEMENT_PRIMARY_GAME_MODULE. Echohearts uses ECHOHEARTS_API; EchoheartsRebearth uses ECHOHEARTSREBEARTH_API. Build main and a development PR may differ. Preserve an explicitly approved module contract; investigate any branch mismatch rather than treating the mismatch as permission to migrate. Never globally replace macros or create competing module names based on a repository title.

## Math and gameplay utilities

Use Unreal types/helpers rather than duplicating engine math. Add reusable utilities only as needed for vector/distance/direction normalization, interpolation/inverse interpolation, clamp/remap, grid quantization/coordinates, spatial lookup, orbital motion, probability, steering, separation/alignment/cohesion, particle attraction/falloff, projectile prediction, collision, movement smoothing, aiming, camera easing and damage falloff.

Handle zero vectors, divide-by-zero, reversed/degenerate ranges, NaN/infinity, negative coordinates, large-world positions and integer overflow. Document units and coordinate spaces. Test behavior and boundaries rather than restating formulas.

## Structural snapping repairs

Locate StructuralSnappingTypes, UStructuralSnappingComponent and related implementation. If absent, record absence and use approved design placement rather than claiming a repair.

Fix malformed includes/reflection/metadata. TArray remains dynamic; metadata does not turn it into a fixed-size array. Provide configurable data and safe defaults. Use correct local/world transforms.

Validate socket occupancy, connection type, distance, orientation tolerance, structural compatibility, collision/overlap, ownership/build permissions, resources, finite values and server authority before placement. Distance alone is insufficient. Preserve future foundations/walls/floors/roofs/ramps/devices scope without implementing all asset families at once.

## Server-authoritative replication validation repairs

Locate UReplicationStateValidator. Client world transforms are requests, not trusted server state. Validate ownership/role, finite values, world bounds, transaction order/replay, allowed movement/placement distance, snap rules, collision, structure ownership, permissions, resource/state conditions and rate limits against server state.

Use appropriate RPC ownership/validation patterns for the actual UE version. Evaluate Reliable bandwidth/queue behavior for high-frequency calls; do not automatically mark movement RPCs Reliable. Keep security/state validation distinct from cosmetic replication. A world subsystem follows world lifetime but is not itself a replicated authority bridge; use approved authoritative GameState/Actors where shared state requires replication.

Reject client/off-thread world-state mutation and nonfinite restoration inputs, preserve stable delegate snapshots and avoid duplicate discovery. Reconcile existing correction PRs rather than stacking obsolete patches.

## Spatial grid repairs

Locate USpatialGridHasherComponent. Store actual cell coordinates, such as FIntVector after checked conversion, as keys; hash values are container lookup aids, not authoritative cell identity.

Implement registration, unregister/removal, movement updates, stale-bucket cleanup, nearby-cell/radius queries and invalid-object handling. Use suitable weak/managed object references and lifetime cleanup. Moving actors must leave prior cells. Test negatives, exact cell boundaries, checked large coordinates, hash collisions, empty buckets and destroyed references.

## Isolated vector processor repair

Locate ExecuteIsolatedDecoupledVectorRegistryProcessor(). Do not assign std::string directly to char. If first-character processing is intended, check token emptiness before indexing. Fix includes, types, size/bounds handling, naming/output and behavior tests.

Determine whether the utility belongs in engine-independent tests/examples or actual UE gameplay. Keep unrelated examples isolated or retire them with provenance; do not force them into the runtime module.

## Linked GitHub Actions failure and regression protection

Inspect complete logs for:
https://github.com/Dlomotion/Echohearts-Rebearth/actions/runs/37146815957/job/112065388540

Reported failure: python 09_Technical/Tools/verify_infrastructure.py infrastructure failed with missing file / Errno 2 / exit code 2. Treat this as a supplied diagnosis to confirm against actual logs and failing commit. The reported Node.js message is a warning, not the alleged root cause.

Compare failing branch/SHA, current main and active PRs. Determine whether the script path, branch contents or both were wrong and whether later commits already fixed them. Do not suppress the error, add a no-op validator or reintroduce an obsolete repair.

Run infrastructure and recovery-plan modes using the script's actual CLI. If absent, emit a clear workflow diagnostic. Ensure the validator checks meaningful conditions and fails when they are violated. Keep hosted/static CI separate from Unreal runtime validation.

Inspect .gitignore and .gitattributes together: Wavefront .obj assets configured for LFS must remain trackable; distinguish them from compiler object outputs with scoped rules. Assert LFS attributes and clean-clone behavior where appropriate rather than claiming LFS pull from a static check.

## Engineering references and supplied videos

Study when accessible:
- https://youtu.be/Jnwm2DvmyPo?is=6MO8JMjI2oiaKbJk
- https://youtu.be/6y0bp-mnYU0?is=5U6tNS674LbakYU5
- https://youtu.be/kZqFS6ldMac?is=qo9eHn3vHv6peQgg

Check current official Epic/Unreal documentation for implemented features and the actual supported engine version. Supplement with credible engineering papers/talks/articles/postmortems and licensed public code where useful. Record source, license/provenance and the original Echohearts decision informed. State inaccessible video/page/transcript access honestly; do not invent its contents or copy protected implementation/assets.

## Interactive prototype routing and requirements

These are requested prototypes, not automatic core-game dependencies. Implement only the bounded assigned prototype after foundational gates, with a clear destination.

| Prototype | Destination and required behavior |
| --- | --- |
| 3D product viewer | Asset inspection for Eco-Kin, equipment, artifacts/buildables: orbit, zoom, reset, lighting, approved material/form variants, desktop/mobile responsiveness. Inspecting partners does not imply selling them. |
| Cursor particle field | Resonance/Niagara experiment: cursor attraction/swirl, trails, color shifts, bounded count/force, clear/reset, background options, screenshot export where supported. |
| Probability simulator | Balance/training tool: dice/coin, trial counts, live histogram, theoretical comparison, reset/animation speed. Bond probabilities must follow authored Kindling rules. |
| Theremin | Resonance audio experiment: X pitch/Y intensity, waveform, reverb, play-area guide, mute and pitch readout; accessible audio initialization. |
| 3D physics playground | QA map: spheres/boxes/cylinders, stacking/bounce, gravity/restitution, grab/drag and collision-stability tests. |
| Warp-speed starfield | Optional presentation/approved sky traversal experiment: pointer steering, speed/density, boost/streaks, reduced motion and scalability. Does not establish geography. |
| Top-down space shooter | Proposed buildable/obtainable in-world arcade: waves/shooting, multi-shot/shield/speed, lives/score/high score, pause, parallax/muzzle feedback, keyboard/gamepad/pointer and appropriate local persistence. |
| Astronomical viewer | Lore/developer visualization: orbit bodies, time scale, labels, focus camera, pause/trails/info panels; no invented canonical celestial layout. |
| 3D platformer | Traversal test: run/jump, conditional double-jump, moving platforms/hazards, checkpoints, target/collectible counts, death/restart; temporary camp save only if approved. |
| Boids | Ecology/AI testbed: separation/alignment/cohesion, obstacle avoidance, bounded population, controls and profiling. |
| Portfolio | Existing external studio/project web layer; not a mandatory packaged-game system. |
| Prime explorer/function grapher/cellular automaton | Developer/educational terminal tools; require explicit design reason for gameplay integration. |
| Vector-field plotter | Safe parsed equations, density/scale controls, presets, play/pause/reset, animated flow lines/particles, pan/zoom and hover vector values. Never use unsafe eval. |
| Music visualizer/chord progression | Audio tools or approved music interactions, bounded rendering and understandable controls. |
| Fluid ripples | Water/Resonance/shield/scan/impact material experiment; test visual/performance suitability. |
| Revenue dashboard | Business/developer analytics; adapt visualization to Sanctuary economy only where canon supports it. |
| SaaS landing/event website | External studio/marketing layer; no default Unreal packaging or publication from this brief. |
| Low-poly terrain flight | Streaming/collision/traversal test, altitude/speed HUD, readability and day/night; does not prove world streaming. |
| Procedural fractal tree | Flora/vegetation/restoration growth experiment; bounded generation and coherent ecology. |
| First-person maze | Navigation/dungeon/accessibility test: collision, collectibles, explored minimap, optional timer, exit/win and reset. |
| Choropleth map | Rebearth region/ecology/restoration map: metric switch, legend/tooltips, zoom/pan/reset, selection/details and clearly illustrative sample data. Do not insert real-Earth political geography as game canon. |

Separate model/data, validation, sampling/projection, renderer, animation and UI. Bound particles/sampling/simulation. Keep presentation experiments and business analytics outside authoritative runtime gameplay. Maintain tools after the slice when they serve ongoing QA.

## Performance, accessibility, security and save contracts

Profile major systems on stated hardware; do not assume 60 FPS from source inspection. Scale particle/AI population, effects/shadows, simulation density and draw distance. Prefer events, pooling and measured budgets where appropriate.

Build remappable controls where feasible, readable text, keyboard/controller navigation, touch suitability, reduced motion, sensitivity/inversion, captions/subtitles, non-color-only feedback and fast onboarding. Test actual input and accessible feedback.

Use versioned save/profile schemas, stable IDs, migrations, interrupted-write recovery and authority checks for cloud sync. Do not claim cross-play/cloud-save/backend security from interfaces alone. Telemetry must distinguish gameplay/performance/engagement and anti-cheat evidence, respect access/privacy requirements and avoid client-trusted enforcement.

PR #20 platform/publication contracts require separate repository, target hardware, networking/save and EPUB render evidence. Preserve released EPUB 3.3 baseline unless an authoritative update is intentionally adopted; ebook/device/storefront/accessibility validation is independent of game CI.

## Testing and runtime evidence

Run meaningful pure-domain tests with the existing runner, and Unreal Automation tests where appropriate. Cover math invalid/boundary cases, spatial registration/removal, snapping rules, authority/replay/rate/finite-value validation, NPC/player state transitions, dummy damage/reset, save/version recovery and deterministic behavior where required.

Only run commands that exist for the inspected repository. For the standalone Echohearts track, inspect CMakeLists/tests before using cmake -S cpp -B build -DCMAKE_BUILD_TYPE=Release, cmake --build build --parallel and ctest --test-dir build --output-on-failure. For web work, discover actual package scripts/build arrangement; do not invent npm install/typecheck commands for a single-file browser repository.

UE5.8 Windows gate when licensed/compatible environment exists:
1. Exact clean clone and recorded SHA; git lfs pull where applicable.
2. UHT success and Development Editor Win64 compile.
3. Editor launch and actual required map load.
4. PIE for at least 30 seconds; player movement, NPC navigation and dummy hit/reaction checks.
5. Issue #10 humanoid/Eco-Kin animation, terrain contact, hit location and Kindling/ecology evidence.
6. Server/client authority and replication tests where applicable, with actual network conditions.
7. Development Win64 cooking/package and packaged launch.
8. Save/load/recovery and measured performance evidence where applicable.

Retain commands, logs, exit codes, exact SHA/platform/engine version, artifacts and real screenshots where useful. If unavailable, mark RUNTIME VALIDATION REQUIRED / NOT YET VERIFIED. Never fabricate compiler/UHT/Automation/PIE/network/package/profile results. Static validation, mock images/files and synthetic latency simulation are not runtime proof.

## Attachment handling

Chat scratch paths are temporary and are not repository assets or portable Copilot inputs. Check existence/readability before use. Recover original bytes, inspect the actual image, map it to the approved identity and provenance, and version edits separately. Do not replace approved art because a source is missing.

The chat reports file_00000000ed0062309c7d3ff2fce23f01.png as unavailable: PENDING IMPORT, request re-upload, do not claim recovery/use. Other listed chat attachments require explicit repository import/provenance before Copilot can use them. This brief does not import or visually approve the images.

## Required Copilot response for every implementation pass

Before editing: identify relevant existing files, exact branch/module, source-of-truth requirement, concrete problem and bounded acceptance criteria.

Then implement the assigned coherent correction/feature where possible. Report:
- files changed and classes/functions added/modified;
- error root cause and resulting behavior;
- exact checks/tests run, exit/results and relevant evidence;
- remaining warnings, inaccessible references and missing prerequisites;
- runtime/hardware/browser/save/network/EPUB validation still required;
- smallest logical next implementation step within the authoritative production sequence.

Do not call code compiled, VERIFIED, production-ready, secure, optimized, network-safe or packaged without evidence supporting that specific claim. Preserve working canon and architecture. The goal is a progressively playable Echohearts: Rebearth.

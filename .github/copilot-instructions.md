# Echohearts / Eco-Kin — GitHub Copilot Repository Instructions

## Authority and mission
Treat this repository as part of the unified Echohearts: Rebearth development ecosystem. The canonical authority is `Dlomotion/Echohearts-Rebearth`; when this repository conflicts with it, preserve the local implementation until the conflict is documented, then reconcile toward the canonical repository rather than silently inventing canon.
Build a playable, maintainable, secure, accessible, cross-platform Echohearts game and supporting web/tooling. Repair existing code before adding disconnected demos. Prefer the smallest production-safe vertical slice and measurable runtime evidence.

## Canon lock
- Target planet: Rebearth. Creature classification: Eco-Kin. Player: Frequency Tamer / Core-Binder.
- Nature is a Legendary Humanoid-Kin with conditional Mutations, not a monarch.
- Core attributes are Vibrance, Density, Harmony, and Purity. Do not replace them with generic RPG attributes in canon-facing systems.
- Preserve the Anima-Link bi-directional strain loop between player and Eco-Kin.
- Production engine target is Unreal Engine 5.8, clean object-oriented C++ with Blueprint-facing interfaces/data where appropriate.
- Preserve the 125-ID Permanent Eco-Kin Dex as production-roster authority. Historical/prototype naming pools are archives, not automatic canon.
- Animal Eco-Kin require coherent animal anatomy; Humanoid-Kins remain distinct.
- Do not import names, characters, creatures, maps, lore, protected expression, proprietary code, or franchise identity from outside games.

## Current gameplay rules
- PvE/adventure roster: up to 8 unique Eco-Kin.
- PvP roster: up to 6 unique Eco-Kin.
- No duplicate Eco-Kin in battle rosters.
- Worker/task automation starts with up to 5 Eco-Kin and expands when the applicable farm, homestead, Sanctuary, settlement, or work area levels up.
- Support quests/expeditions, seeding, watering, harvesting, wood gathering/processing, livestock care, milking, shearing, resource gathering, production, trade, Gold/economy restoration, sickness, care, recovery, storage, breeding stations, and healing/incubation.
- Legendary Eco-Kin are unique and cannot be bred; they are discovered through authored world/story/event/encounter rules.
- Breeding must reuse established inheritance, personality, mutation, Purity, Bond/Kindling, evolution and ecosystem rules.
- Hometown is a later story/DLC arc: a villainous team destroys the hometown, driving survivor, investigation, rebuilding, farming/economic recovery, and broader Rebearth consequences.
- Core loop: Explore → Restore/Purify → Encounter/Bond → Build squads → Battle → Gather → Farm/Build → Assign workers → Produce/Process → Trade/Economy → Care/Heal → Breed eligible Eco-Kin → Upgrade areas → Increase worker capacity → Rebuild communities → Unlock regions → Advance story.

## Engineering behavior
Before changing code, inspect the actual repository, build scripts, tests, configs, schemas, and nearby implementation. Do not guess file names, APIs, engine modules, or successful build state.
Audit C++/Blueprint/web code for compile/API correctness, Unreal ownership/lifetime/GC, delegates, threading, RPC authority and ownership, replication/prediction/desync, bandwidth, save/versioning/migrations, deterministic generation, World Partition/streaming, identifiers, error handling, security/exploit surfaces, accessibility, CPU/GPU/memory/network cost, deprecated APIs, duplicated systems, and tests that can false-pass.
Prefer focused fixes over rewrites. Preserve working architecture unless evidence justifies a change. Add or update tests for behavior changed.
Never call a feature VERIFIED without actual repository/build/test/runtime/browser/profile evidence. Otherwise report NOT YET VERIFIED and state the missing evidence.

## Research and code-quality rule
When evidence is missing, consult current official Unreal/Epic or relevant vendor documentation first. Public GitHub/open-source projects, engineering articles, papers, talks, and released-game postmortems may be used to learn transferable patterns only.
Check license and provenance before adapting public code. Do not paste code blindly. Reimplement concepts in original Echohearts architecture and naming. Record useful sources and why they affect a decision.
“Perfect the code” means continuous evidence-based improvement: correctness → tests → security → performance → accessibility → maintainability → gameplay quality. Never claim literal perfection.

## Visualization/debug tools requested
Implement production-quality developer visualization tools where appropriate:
1. Choropleth world-state explorer: sample country data, metric switcher, continuous legend, hover tooltips, click selection, pan/zoom/reset, and selected-country detail panel. Keep the data/projection layer geography-agnostic so it can later visualize Rebearth regions/biomes and Vibrance, Density, Harmony, Purity, restoration, ecology, settlement/economy, or telemetry metrics.
2. Vector-field laboratory: editable 2D field F(x,y)=<P(x,y),Q(x,y)>; safe expression parsing/validation; immediate redraw; arrow-density and magnitude/scale controls; presets including rotation, sink, source, saddle and wave; animated particles/flow lines; play/pause/reset; pan/zoom; hover readout for x, y, Fx, Fy and magnitude. Invalid equations must show an inline error and never crash rendering.
Separate data/model, validation, sampling/projection, renderer, animation and interaction/UI. Bound sampling/particle counts, memoize expensive work, isolate animation from UI state, support keyboard interaction/reduced motion, and add tests. Sample data must be clearly labeled illustrative.

## Repository collaboration
These repositories are related and should be considered when a task spans them:
- Dlomotion/Echohearts-Rebearth — canonical game/canon authority.
- Dlomotion/echohearts-web — playable/supporting web implementation.
- Dlomotion/Echohearts-Ecokins — Eco-Kin-related implementation/reference.
- Dlomotion/ECO-KIN-Game — game/prototype implementation/reference.
- Dlomotion/ECHOHEARTS-REBEARTH- — related private development repository.
- Dlomotion/ECHOHEARTS-REBEARTH-BUILD- — related private foundation/build repository.
- Dlomotion/Echohearts — related web/reference repository.
Do not assume another repository is synchronized. Inspect it before proposing cross-repository changes. Do not overwrite a newer implementation with an older prototype.

## Definition of done
For each task: identify the source-of-truth requirement; inspect existing code; implement the smallest coherent correction/feature; run the strongest available static/build/test/runtime checks; document failures honestly; preserve canon; and leave an exact next verification step. No disconnected demo code and no fake verification.

© 2026 Into Deep Studios and Donta L. Owens. All rights reserved.

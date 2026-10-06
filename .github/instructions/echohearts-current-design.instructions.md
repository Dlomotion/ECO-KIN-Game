---
applyTo: "**"
---

# Echohearts: Rebearth — Current Design Sync

Last synchronized: 2026-10-06
Repository role: **LEGACY_GAME_SUPPORT**

Do not fork canon here. The canonical text contracts live in `Dlomotion/Echohearts-Rebearth`.
Executable UE5.8 implementation/evidence belongs in `Dlomotion/ECHOHEARTS-REBEARTH-BUILD-` unless ownership is explicitly reassigned.

## Read before creating or fixing code

The latest user-requested design intake adds three connected workstreams:

1. **Master Inventory / Materials / Shops Registry**
2. **Upgrade Highlights package**
3. **Echo Egg system and visual collection**

Canonical source files in `Dlomotion/Echohearts-Rebearth`:
- `04_Systems/Inventory/ECHOHEARTS_MASTER_ITEMS_MATERIALS_REGISTRY_2026-10-06.md`
- `04_Systems/ECHO_EGGS_AND_UPGRADE_HIGHLIGHTS_2026-10-06.md`

The inventory registry contains **737 category entries / 694 unique named entries / 28 categories**. Preserve each entry's status. A Legacy, Retired, Rename Required, alias, prototype, or cross-reference entry is not automatically public canon and must not be silently promoted.

## Canon locks

- Planet: **Rebearth**
- Creature class: **Eco-Kin**
- Player: **Frequency Tamer / Core-Binder**
- Core attributes: **Vibrance, Density, Harmony, Purity**
- Preserve **Kindling** and the **Anima-Link** bi-directional strain/damage loop
- A.E.G.I.S. is the physical bracer/interface
- Nature is a Legendary Humanoid-Kin with conditional Mutations; never call Nature a Legendary Monarch
- The 125-ID Permanent Dex is roster authority
- Do not create generic Strength/Mana/Agility/Speed replacements
- Do not import outside franchise terminology, characters, proprietary mechanics expression, code, UI, or art

## Current upgrade highlights

Treat these as implementation targets, not unverifiable marketing claims:
- **Restored World Visuals** — richer restoration states, foliage, water, weather, lighting, biome readability, scalable performance
- **Resonance Combat Flow** — smoother authored movement/combat, readable hit feedback, Anima-Link strain feedback, server authority
- **Resonance Skill Paths** — Vibrance/Density/Harmony/Purity-based progression only
- **A.E.G.I.S. Expansion** — scanning, Echoprints, anomaly/material tracking, restoration diagnostics, Echo Egg care readouts
- **Sanctuary Building 2.0** — modular building, farming, water, care, power, logistics, nursery/incubation
- **Echo Egg Incubation & Nursery** — ethical care, lineage validation, no automatic new species creation
- **Eco-Kin Animation & Terrain Contact** — locomotion, contact, notifies, reactions, ecology interactions
- **Appearance Weave** — cosmetic-only appearance overrides with no combat/stat advantage
- **Photo Mode & Echo Archive** — original capture/archive UI, accessibility, no authority bypass in multiplayer
- **World Pulse / Quest Tracking** — restoration %, Blight pressure, boss gates, material/recipe tracking, Egg care tasks
- **Inventory / Marketplace Overhaul** — stable IDs, trade restrictions, atomic server transactions, anti-duplication
- **Performance / Stability / Accessibility** — save/load, crash diagnostics, bounded replication, scalable settings, readable multimodal cues

## Echo Egg registry

Echo Eggs are developmental/incubation items, not capture devices, random species generators, or guaranteed rarity containers.

Core variants:
- **Aero Echo Egg** — airflow and pressure care
- **Aura Echo Egg** — calm/Harmony-oriented care
- **Glaze Echo Egg** — cold/moisture stability
- **Pyre Echo Egg** — controlled warmth and thermal venting
- **Radiant Echo Egg** — clean-light/Purity care
- **Shade Echo Egg** — low-light, low-disturbance care
- **Terra Echo Egg** — mineral bed and vibration stability
- **Tide Echo Egg** — Torrent/Hydro, humidity and clean-flow care
- **Verdant Echo Egg** — Flora, living soil and plant cover
- **Volt Echo Egg** — Voltic, grounded controlled charge
- **Resonant Echo Egg** — neutral/stable pre-resolution shell
- **Sanctuary Echo Egg** — high-quality care-state shell, not a species/tier
- **Prismatic Echo Egg** — rare multi-signature shell; outcome must still be an eligible Permanent Dex identity
- **Ancient Echo Egg** — preserved provenance state; does not imply Legendary
- **Sovereign Echo Egg** — rare event-grade shell; it must never produce a breeding-locked Legendary, god/entity, Nature, or Event Sovereign by ordinary incubation

A **Blight-Stressed Egg** is a rescue condition, not a collectible rarity. Purify and stabilize it; do not reward suffering with exclusive power.

Species with non-egg biological reproduction remain species-appropriate. Do not force every Eco-Kin into an egg lifecycle.

## Echo Egg runtime/data rules

- Stable definition IDs and save versions
- Eligible Permanent Dex IDs / lineage validation
- Gameplay Tags for Resonance/environment states where appropriate
- server-authoritative acquisition and hatch resolution
- bounded, auditable randomness if used
- no client-supplied hatch outcome
- breeding-locked records fail closed
- atomic inventory consumption + hatch commit
- reconnect/crash recovery cannot duplicate, delete, or reroll a committed outcome
- newly hatched Eco-Kin retains individual identity/history and still requires care/Kindling
- shell art/material/VFX/SFX are presentation data, not hidden combat power

## Visual direction from the latest approved concept pass

Upgrade-highlight screens:
- dark Rebearth night/forest surface
- fine gold framing and original Resonance glyphs
- strong readable two-column hierarchy
- individual icon medallions per upgrade
- no copied layout text, symbols, logos, or external franchise names

Echo Egg Collection:
- living branch/nest construction
- bioluminescent foliage
- star-like Resonance motes
- distinct shell material for each egg family
- text + icon/pattern identification; never color alone
- collection, incubation, care-condition, lineage, nursery-capacity, rescue/purification, and archive screens

## Inventory implementation rule

Before implementing an item, search the canonical registry entry and preserve:
- display name
- category
- canon/status field
- aliases
- crafting/source notes
- shop/trade rules
- whether it is a material, relic, tool, trap, station, weapon, armor, consumable, currency, cosmetic, key artifact, or legacy record

Never convert the whole historical registry into active runtime content at once. Import only approved subsets and validate stable IDs, save migration, inventory stacking, source acquisition, tradeability, and references.

## Code-fix behavior

When asked to create or fix code:
1. inspect the owning repo, branch, implementation, tests, workflows, and call sites;
2. search the seven Echohearts repos before duplicating a system;
3. identify the root cause from real diagnostics;
4. make the smallest coherent patch in the owner repo;
5. preserve canon/data contracts and stable IDs;
6. add/update tests and validation;
7. run every available static/CI check;
8. never suppress a required failure to make CI green;
9. report exact evidence;
10. use **NOT YET VERIFIED** for anything still requiring UE5.8 build/runtime/network/save/performance proof.

## Language ownership

- **C++ / UE5.8**: production game/runtime systems
- **TypeScript / JavaScript**: web, presentation, editor/support tooling where the repo already uses them
- **Python**: build/validation/data-processing/tooling
- **C#**: legacy/prototype/support tooling only unless an authority contract explicitly promotes a use
- Do not rewrite a working system into another language merely because that language is available.

## Final instruction

Use the new registry, upgrade highlights, and Echo Egg contracts as current project context. Create requested features only in the repository that owns them, keep changes reviewable, fix code from evidence, and never create a second canon/runtime authority.

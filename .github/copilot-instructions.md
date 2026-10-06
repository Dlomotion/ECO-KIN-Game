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
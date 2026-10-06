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

## Unified Echohearts creation and code-repair directive — 2026-10-06

This repository participates in one Echohearts: Rebearth production family. GitHub Copilot must help **create requested game work and repair code** inside established ownership and evidence gates.

### Authority
- `Dlomotion/Echohearts-Rebearth`: canon/story/design/system-contract authority.
- `Dlomotion/ECHOHEARTS-REBEARTH-BUILD-`: executable UE5.8 runtime/build/evidence authority.
- `Dlomotion/echohearts-web`: web/presentation.
- `Dlomotion/Echohearts-Ecokins`: Eco-Kin support/archive.
- Other listed repositories are legacy/prototype/support unless an authority document says otherwise.

Do not create duplicate runtime modules, GDDs, Dexes, canon, save schemas, networking stacks, or build pipelines.

### Locked identity
Preserve Rebearth; Eco-Kin; Frequency Tamer/Core-Binder; Nature as a Legendary Humanoid-Kin with conditional Mutations; Vibrance/Density/Harmony/Purity; Anima-Link; Huma-Link; A.E.G.I.S.; the 125-ID Permanent Dex; real-time third-person campaign combat; carry 8 / 3 active / no duplicates when the active data contract agrees; and UE5.8 C++ as production runtime.

Older or candidate material—Meridian tech/Nodes, Time-Echo ruins, E.C.O. Sentinel, Cosmo-Seraph/AstraVore-class concepts, gardens/care, relic/idol/fusion/reversion ideas, branching endings—must pass canon review before implementation.

### Create/fix code
1. Read local instructions and source-of-truth docs.
2. Inspect the actual implementation, call sites, tests, build scripts, workflows, branch, and related issues/PRs.
3. Diagnose from compiler/UHT/UBT/UAT/test/runtime/log evidence.
4. Consult current official docs and reputable public samples/issues when needed; never copy proprietary code or franchise identity.
5. Fix the smallest coherent root cause and preserve compatibility unless migration is explicit.
6. Add/update tests or validation.
7. Run available checks and report what passed.
8. Use **NOT YET VERIFIED** for claims lacking required runtime/build evidence.

### Language roles
- C++: UE5.8 gameplay/runtime, replication, AI, save/network systems.
- TypeScript/JavaScript: web/browser/tooling; prefer TypeScript.
- Python: build helpers, validators, automation, data/content processing.
- C#: legacy/prototype/support tooling unless explicitly promoted by an authority contract.

Audit lifecycle/reflection, Build.cs/modules, authority/RPCs, prediction/replication, validation, stable IDs, serialization/migrations, thread/UObject safety, async loading, World Partition, memory/performance, accessibility, security, packaging/platforms, cloud/save boundaries, UI, AI, animation/VFX/audio, and data/schema integrity as applicable.

Trace gameplay changes end-to-end:
**input -> authority -> state mutation -> replication/save -> UI/VFX/audio feedback**.

Use `STATIC CHECK PASSED`, `REPOSITORY CONTRACT PASSED`, `CI PREFLIGHT PASSED`, and `NOT VERIFIED — UE BUILD/RUNTIME EVIDENCE REQUIRED`. Use `VERIFIED` only with matching evidence.


## Historical Eco-Kin naming pool + COBOL/BASIC directive — 2026-10-06

### Authority and archive rules
- The **125-ID Permanent Eco-Kin Dex** remains the production roster authority.
- Preserve the **1,120-name Master Historical Naming Pool** as an archive of created names, prototypes, forms, evolutions, mutations, regional variants, rename candidates, cosmetics, bosses/entities, legacy labels, and retired references.
- Never auto-promote a historical name into the Permanent Dex. Promotion requires explicit canon review, a valid stable EcoKinID or approved Forms Registry relationship, anatomy/identity review, originality/IP review, data validation, and production evidence.
- Historical names that collide with outside franchises, protected characters, direct mythology imports, or other zero-derivative restrictions must remain quarantined under 99_Reference_Retired_Needs_Redesign until replaced with original Echohearts nomenclature.
- Do not delete, silently rename, or overwrite historical names merely because they are not current canon. Preserve provenance and redirects.
- Before creating a new Eco-Kin name, search the Permanent Dex, Forms Registry, and this historical pool to avoid duplicates and accidental identity replacement.

### Master historical alphabetical naming pool
**#**  
15 Karat

**A**  
Aardhymn, Abysslurk, Abyssola, Abyssquill, Aeralune, Aerobloom, Aerobull, Aerocrest, Aerodart, Aerogale, Aerokite, Aerolynx, Aeropierce, Aeropteryx, Aeropuff, Aeroraptor, Aeroray, Aeroscale, Aerospike, Aerospine, Aerostrike, Aeroterra, Aerotusk, Aerovelon, Aerovine, Aerovore, Aerovortex, Aerowasp, Aerowisp, Aerowyrm, Aeruin, Aether-Valkyrie, Aether-Wisp, Aetherwing Seraphin, Aevaswift, Africanized Queen, Anstronaut, Ant, Anteater, Antelope, Antler, Aqua-Drift, Aquaceros, Aquafinn, Aqualin, Aqualume, Aqualynx, Aquanith, Aquatyr, Aquoray, Aquorgnash, Arborveil, Armadillian, Ash-Brawler, Astraea Lumicore, Astraelune, Astravault, Astryx, Atomic Horror, Auraglider, Aural, Auralyss, Aurelior Prime, Aurelius-Prime, Aureon, Aurora Basin, Aurorabloom, Auroraeel, Aurorafin, Auroraguard, Aurorale, Auroralis, Aurorarch, Aurorash, Aurorisk, Aurunefer, Axoloti, Azura Turtle, Azurane, Azurbuzz, Azure Soul, Azureon Shell, Azurtle Crest.

**B**  
Bananaza, Barkguard Accent, Basalt-Crusher, Basin Sentinel, BeAts, Bees Gees, Beetle, Billstalk, Black Swan, Blackflash Thylundra, Blightfang Vezreth, Blightide, Blighttad, Blizzara, Bloomantis, Bloombud, Bloomplate Nurture, Bogbloom, Bogtank, Boogie Woogie, Boomturt, Bot, Bot Core, Botan-Bug, Breezephyr, Breezette, Briarshade, Brimclaw, Bromebruin, Bubba, Bubbleep, Bugsaboom, Buttafly.

**C**  
Cadensora, Calla Lilly, Calycko, Candelbra, Canopulse, Canopyrex, Canopyrus, Canopyvault, Capyflow, Cattapilla, Cattery, Causticpulse Olmnisense, Celestefish, Celestidrift, Celestrake, Celestrider, Chacron, Chaos Howler, Chaos Woof, Cherry Blossom, Chesster, Chimpanzion, Chip Ship, Chorusvine Accent, Chronos-Kyros, Chronydon, Cinderclaw, Cindermaw, Cinderplate Defender, Cinderpup, Cindersnout, Cindervault, Citrakhan, Clearcycle Eonotara, Clearsap Accent, Clearstorm Thylundra, Clockedit, Cloudpip, Coluglyph, Coluglyph Skyweaver, Continental Wake, Coral Owl, Coralguard, Coralith, Corallith, Coralomni, Coralshell, Coralsinge, Coraltide, Coralug, Coralvine, Coralynx, Corrupelle, Corrupted Ferronix, Corvexis, Cosmo-Seraph, Cragbeetle, Craghide, Cragleon, Cragmunch, Cragquill, Cragrhino, Cragtusk, Crane, Crowncurrent, Crownsting Matriarch, Cryopuff, Cryovulp, Crystalaxe, Crystalbite, Crystalisk, Crystallurk, Crystallux, Crystalsikr, Crystaltimber, Crystalux, Crystalynx, Crystephin, Crystikoi, Crystogon, Cyclops.

**D**  
D. Frog, Dalmatian, Dammaker, Dandecrown, Dandelift, Dandelion, Dante Inferno, Dappletide, Deadwave Kakaphonic, Deep Chorus, Deepclaw, Deer Don, Demon, Dewfawn, Doctorpua, Doll Scorched, Dr. Evil Sylar, Draggong, Dreadroot, Dryad, Dryara, Duke Drake, Dullahan, Duneskitter, Duneslash, Dunespike, Dunesprig, Dunetrunk, Dunewraith, Duskfin, Dust Bunny, Dusthollow.

**E**  
Ebonmaw, Eerie, Eerivex, Eerloom, Electroid, Elephiant, Ember, Ember Heart, Ember Moth, Emberback, Embercrab, Embergaunt, Emberhare, Emberpup, Embertail, Emberwing, Eonotara.

**F**  
Fairytail, Fairytell, Falcon, Falcon Orange, Falcone, Fawn Don, Fawnelle, Featherfright, Fernbeetle, Fernglider, Ferronix, Ferrumwarden, Finalize, Firefly, Flaminingo, Flare-Vulpix, Flarevane, Flashhorn, Floaureign, Floauwer, Florafinity, Florisprig, Floroyal, Fourfold Year, Fox Fur, Frostbite, Frostclaw, Frosthale, Frosthide, Frosthorn, Frostquill, Frostroot, Frostseal, Frostshard, Frosttusk, Frostveil, Frostwalrus, Frostwraith.

**G**  
Galactorra, Galegriff, Galestorm, Gargantuan, Gazillion, Geckalord, Geckalyx, Gecklorix, Geoloom, Geomunch, Geotank, Geowurm, Gerenreach, Gerenreach Crownforager, Ghost, Ghoul, Glacialugg, Glacibear, Glacibot, Glacidon, Glacidrill, Glacierkin, Glacieroo, Glacierune, Glacifang, Glacifer, Glacifin, Glacifort, Glacifur, Glacipack, Glaciram, Glaciroam, Glacirock, Glacitank, Glaciwal, Glassbill Shoebastion, Glasshorn Gerenreach, Glassmantle Korravault, Glassplate Limulock, Glassskin Siltamender, Glassveil Coluglyph, Glassvoice Kakaphonic, Glidefin, Glimbit, Glimmerbill, Glimmerpup, Glimmider, Glitchfrost, Gloomfin, Gloomstalk, Glow Worm, Glowyrm, Gnome Gazette, Gnome Rock, Goldband Termitune, Golden Fish, Goo Goo, Googley Eyes, Gopher Goshen, Granclad, Granitank, Granvore, Graveglow, Gravemaw, Graviklaw, Gravipaw, Gravipod, Gravistrider, Gravitide, Gravitonk, Gravityx, Gravlith, Gravypod, Greedyig, Griffin, Grim Stone, Grimbloom, Grimburrow, Grinmlin, Grove-Beetle.

**H**  
Hammerwake, Hamstring, Handimon, Hands Shake, Harp Harmonies, Hawke, Headwater Bulwark, Hedgeshog, High Voltage, Hippo, Hisbiscuits, Hive Spark, Hollowhunger Termitune, Horizon Crown, Horizon Veil, Hounding, Huntresson, Hushrot Aardhymn, Husky, Hydra, Hydrashell, Hydrothorn.

**I**  
I Scream, Icesentinel, Igneelisk, Igniclaw, Ignifin, Ignirock, Igniserpent, Ignishell, Ignisoul, Ignispike, Inkmire Vitrivane, Iron-Paladin, Iron-Spark, Ironbeak, Irondeer, Ironhide.

**J**  
Jackalope, Jelly Jellyfish, Jen, Jester in the Box, Jesteroy, Jewel.

**K**  
Kakaphonic, Kakaphonic Nightchorus, Kangzaroos, Kelpteris, Ken, Kendo, Kharuvane, King Corso, King Luthar, King Luther, Kitty, Knight, Korravault, Krabs.

**L**  
Lady Whispers, Lamp, Lanternworm, Lavabat, Lavabuzz, Lavaclaw, Lavafang, Lavalynx, Lavamite, Lavasaur, Lavascamp, Lavashark, Lavaslug, Lavatyrant, Leaf Sheep, Leafguard, Lela, Lemuer, Leon, Leonclaw, Leoncub, Leonguard, Leonix, Leonix Solcrown, Leopaerd, Leviacrest, Leviakresl, Likeness, Limulock, Limulock Shorewarden, Lioness, Lioness Apex, Litty, Lobster, LolLlama, Lorium, Loyalkin, Lumbristell, Lumi, Lumibloom, Lumifae, Lumiflora, Lumifly, Lumifrog, Lumikoi, Lumina, Luminae, Luminaeel, Luminarch, Lumincrab, Luminectar, Luminel, Luminelk, Luminella, Luminelle, Lumineth, Luminflutter, Luminhare, Luminight, Luminite, Luminix, Luminomoth, Luminowl, Luminreef, Lumipint, Lumipod, Lumipollen, Lumipup, Lumiseed, Lumishroom, Lumisprite, Lumistag, Lumitail, Lumiwisp, Lumoray, Lumowisp, Luna Moth, Lunamoth, Lunar, Lunara, Lunaraith, Lunarious, Lunatik, Lunavelle, Lunawisp, Lunaz, Luphantom.

**M**  
Maat, Macaw, Mad Scientist, Magma-Golemx, Magmamite, Magmancer, Magmaroach, Magmaroar, Magmaweld Golem, Magmaworm, Magmorph, Magmorray, Magmusk, Magnapod, Magnash, Magnetar-Titan, Magnetarion Ward, Maize Fortune, Majestik, Mallard, Malon-X, Malon-X the Ink-Ghost, Mamba Kobe, Mamba Kobra, Mandarinis, Mandarion, Mangolden, Mantiz, Marispaw, Marisprit, Marmara, Marrowl, Maxwells, Mcterritorial, Medusa, Membrakit, Mermaid, Mermain, Minnie Ripton, Mireblob, Mirebloom, Mirecoil, Mirefrog, Miregator, Miregill Pelaglyph, Miregorge, Miregorger, Miregulp, Mirehiss, Mirejaw, Mirestomp, Mirevell, Mirewisp, Mistbuck, Misteon, MoeJoe, Moltide, Moon-Walker, Moondrake Umbrelune, Moongoss, Moonpuff, MoonWalker, Morg-An, Morg-An the Thorned Rebel, Morrowind, Mossbeast, Mosschick, Mossmask, Mossmunch, Mossprout, Mottlit, Moundseer, Mousier, Mt. Rush, Mummie, Murmlet, Mustang, Mycelith, Mycodrip, Mycoshade.

**N**  
Nature, Nature Prime, Nature Prime Guardian, Nature Seedling, Nature Verdant, Nature’s Guardian Titan, Nebula, Nebulark, Nebulark Voidwing, Nebulord, Nerekth, Nexaris, Night Angel, Night Owl, Nightgnaw, Nightlurk, Nightpetal, Nightsprout, Nightstalk, Nightveil, Nimbloom, Ninabite, Nivrak, Normandy, Nova, Nullwake, Nulvora, Nurture.

**O**  
Oceanus, Octorpus, Olmnisense, Olmnisense Deepwarden, Omni-Bot Frame, Opal, Oracle, Oral, Orcanize, Origon-Null, Orokharn, Osiris.

**P**  
Palmatyr, Panda Panda, Pangobunker, Pangolance, Pangolin, Panther, Parish, Paw, Peacockochu, Peariguard, Pearl, Pebblegill, Peepfloe, Pelaglyph, Pelaglyph Tidevault, Peppa, Perchara, Perronix, Phoenix, PI-RAT, Pickled Wasp, Pigcasso, Piglot, Pin Stripe, Pinguin, Pinky Bear, Piplin, Plainsman, Poison Ivy, Pola Bear, Polarised, Pondhalk, Poodle D., Poodle Moth, Poyzin Ivvee, Primordash, Prince, Princeton, Prismcurrent Pelaglyph, Prismcurrent Vitrivane, Prismgill Olmnisense, Prismhorn, Prismveil Veylugo, Puddlepeep, Pupular, Pyraboar, PyraLeaf, Pyraphant, Pyratyrant, Pyravore, Pyrewolf, Pyrixis, Pyroduck, Pyrofawn, Pyrogator, Pyromane, Pyroquill, Pyroterra.

**Q**  
Quakecrab, Quakehog, Quakelurk, Quaketail, Quaketurt, Quaketusk, Quarrant, Queen Cobra, Queen Corgi, Quickleaf Accent.

**R**  
Rabbit, Rainhart, Ramos, Ranger Bat, Raven, Reaper-Skull, Red Panda, Reednote, Reeflantis, Reeflorp, Reeflume, Refined Golem, Resonance Kit, Rhizoquill, Rift-Kin, Riftfray Veylugo, Riftplume Aurorarch, Rimefin, Ringmaster, Rino Rhino, Riptide, Robcoon, Robin, Robo Girl, Robopintic, Rockhide, Rockmunch, Rocktide, Rocktusk, Rookurrent, Rootank, Rootcrawler, Rootglass Aardhymn, Rootstalker, Royal Knight, Rubblewick Joss, Rustbeak Shoebastion.

**S**  
Saigale, Sandsprint, Sandstrider, Scarab, Scarecrow, Scorcherix, Sea King, Sea Queen, Sea Turtle, Sealed, Seaplume, Searhound, SeaShield, SeaShock, Sekhmet, Serpentide, Serpentine, Shadefang, Shadepaw, Shadestrike, Shadolynx, Shadotide, Shadowbeak, Shadowbite, Shadowburr, Shadowburrow, Shadowburst, Shadowdart, Shadowdive, Shadowdrake, Shadowfang, Shadowfern, Shadowfin, Shadowgnaw, Shadowgulp, Shadowisp, Shadowlance, Shadowlurk, Shadowmantis, Shadowmoth, Shadownyx, Shadoworb, Shadowpang, Shadowreef, Shadowrift, Shadowroach, Shadowvore, Shadowwisp, Shadrow, Shardwing, Shellkorp, Sherlock Hound, Shoebastion, Shoebastion Marshwarden, Shredwind Coluglyph, Shroom Seahorse, Siltamender, Siltamender Riverelder, Siltback, Skeleton, Skullkin, Skybellow, Skydart, Skydrifter, Skyjelly, Skyloper, Skyquill, Skyraxis, Skyrhapsody, Skytalon, Skyterrix, Skytortoise, Skyvein Crown, Slagheart Korravault, Slagshield Limulock, Sludgemaw Siltamender, Slym Thicke, Snailer, Snoutap, Snoutzip, Snow Bird, Snow Cone, Snow Owl, Snowlet, Snowstrom, Snuffawn, Soaraptus, Solara, Solarail, Solaraven, Solaraxe, Solarcalf, Solareon, Solarflare, Solarian, Solarion, Solaris, Solariser, Solarisq, Solarix, Solarphant, Solarphere, Solarphoenix, Solbeast, Solbeetle, Solcrab, Soldragon, Soldrifter, Solglide, Solguardian, Solkeeper, Sollumen, Solmane, Solmarrow, Solmite, Solorion, Solray, Solrider, Solserpent, Solstalis, Solsylph, Soltalon, Soltortus, Solvore, Solvyrion, Solwisp, Solwraith, Space Bunny, Spacialis-Zea, Sparkyle, Spectra Aurora Emperor, Spectra Chick, Spectra Chicks, Spectra Glidefin, Spectra Glitchfrost, Sporeling, Sporuling, Sprigbeat, Spritz, Sproutkin, Sproutling, Sproutlume, Sproutneck, Squiggly, Squirrel, Stag Don, Starfin, Starflit, Starhaven Perch, Starvault Spires, Stillseason Eonotara, Sting Wreck, Stone-Treader, Stoneback, Stoneburrow, Stoneguard, Stonegulk, Stonehide, Stonejug, Stonelug, Stonemaw, Stonemite, Stonequill, Stonetail, Stonetusk, Stormember, Stormhare, Stormjelly, Stormling, Stormpup, Stormwyrm, Stud Muffin, Sunbride, Sunhoof, Sunseta, Sunspire, Swamps, Swan, Swarm Guard, Sylva-Lynx, Sylvanheart, Sylvornith, Synchronus, Synchronus Omega.

**T**  
T-Rex, Tangeroar, Taquo, Taz, Teddy Reddy, Tempestiga, Tempus-Rex, Termitune, Terra Tusk, Terrabolt, Terralume, Terrawyrm, Terrhino, Tex Rex, Thalassyr, Thermogale, Thermopyre, Thingamabob, Thingamajig, Thornback, Thornmask, Thornquill, Thornshell, Thornveil, THOTH, Thrilla Zombie, Thundaroar, Thundrak, Thylundra, Tidal Bastion, Tidalash, Tidalcrab, Tidalgaurd, Tidalion, Tidalorca, Tidalorp, Tidalspine, Tidaltank, Tidalusk, Tidalux, Tidalwyrml, Tideblot, Tidebutton, Tideclaw Myrmander, Tidefin, Tidelet, Tidelup, Tidequill, Tidewhisk, Tidewisp, Tigrelion, Tigress, Tigrisoul, Tiki, Tortopedo, Torturecannon, Toxibloom, Toxiclaw, Toxifang, Toxifern, Toxiflora, Toxiflow, Toxigator, Toxigulp, Toxileech, Toximander, Toxiraptor, Toxitank, Toxitusk, Toxiviper, Treezing, Tundrahide, Tundraleo, Turntle Turtle, Twilight-Tricker.

**U**  
Ultra Nature Spark, Umbraeel, Umbraleap, Umbralynx, Umbrapaw, Unbound, Uniquecorn.

**V**  
Vaelthundra, Venobloom, Venofang, Venoflow, Venolord, Venomander, Venomite, Venomyss, Venoroach, Venoshroud, Venoslug, Venus Fly Trappin, Verdanok, Verdant, Verdant Nature, Verdant Sage, Verdantapir, Verdanthem, Verdantis, Verdantune, Verdeloth, Verdleaf, Veribark, Veribelle, Veriboar, Veribud, Vericlaw, Vericub, Veridan, Veridash, Veridasher, Veridotter, Veridragon, Veridrake, Veridrench, Veridrift, Veridrill, Veridust, Verifawn, Verifrog, Verigale, Verigaleon, Veriguard, Verihare, Verileap, Verilop, Verilurk, Verilynx, Verimite, Veripad, Veripaw, Veripouncer, Veriraptor, Verirun, Verishell, Verishroom, Verishroud, Verisilex, Verispine, Verisprout, Verithorn, Verithread, Verivine, Veylugo, Vharomaw, Vilecroc, Vilemole, Vilemorph, Vilemoss, Vineclaw, Vinesaur-Rex, Vitrivane, Voidbloom, Voidcrusher, Voidjelly, Voidmanta, Voidmorph, Volcanik, Volcrab, Volcraw, Volquoil, Voltage, Volthor, Voltiki, Vulcan.

**W**  
Walorus, Waste-Kin, Wavehorn, Waveplume, Whaling, Whatchamcallit, White Tiger, Whole-Aquifer Sense, Whole-Canopy Sail, Whole-Gallery Hearing, Wirethorn Gerenreach, Wolfie, Wood Pecks, Wooflet, Wooofy, World Kiln, Worldbloom, Worldroot Chorus, Worldroot Leviathan, Worm, Wormling, Wreckstorm.

**Y**  
Yolk.

**Z**  
Zangoro Seedling, Zebrask, ZebraskA, Zephyloon, Zephyrahn, Zephyray, Zephyrift, Zeptoray.

### COBOL and BASIC engineering directive
COBOL and BASIC are now approved **secondary engineering/tooling languages** for the Echohearts repository family. They supplement but do not silently replace the UE5.8 C++ production runtime.

Use COBOL where its record-oriented strengths are useful:
- deterministic roster/material/accounting-style batch validation;
- fixed-width, CSV, ledger, registry, migration, reconciliation, audit, and report utilities;
- legacy-data conversion and cross-check tools;
- reproducible test fixtures for inventory/economy/save-data contracts;
- CI-side data integrity checks where a COBOL compiler is actually provisioned.

Use BASIC where rapid, readable tooling is useful:
- standalone math/balance simulators;
- migration and data-conversion utilities;
- build/environment diagnostics;
- small regression harnesses;
- prototype visualizers or command-line utilities that do not become shipping gameplay authority.

Language/toolchain rules:
- Detect the actual compiler/dialect already configured in the repository before editing existing COBOL or BASIC.
- If no COBOL dialect is established and a new standalone tool is explicitly needed, prefer portable **GnuCOBOL-compatible** source and document the compiler/version.
- If no BASIC dialect is established and a new standalone tool is explicitly needed, prefer **FreeBASIC-compatible** source and document the compiler/version. Do not silently treat Visual Basic .NET, VBA, QBASIC/QB64, and FreeBASIC as interchangeable.
- New COBOL/BASIC tools should live under an existing tools/validation area. If the canonical folder hierarchy exists, prefer 09_Technical/Tools/COBOL and 09_Technical/Tools/BASIC.
- Exchange data through documented stable schemas and stable IDs; do not scrape presentation text as authority.
- Preserve UTF-8 at boundaries where supported and define field widths/decimal behavior explicitly for fixed-record tools.
- Return nonzero exit status on validation failure and emit machine-readable summaries where practical.
- Add golden fixtures/regression cases for converters and ledger checks.
- Never claim a COBOL/BASIC tool compiled or passed unless the actual compiler/interpreter and tests ran.
- COBOL/BASIC tools must not independently redefine the Permanent Dex, Vibrance/Density/Harmony/Purity, Anima-Link, Huma-Link, save authority, network authority, economy authority, or canon.
- Do not move server-authoritative gameplay, UE object lifecycle, replication, rendering, animation, physics, or packaging out of C++/Unreal merely to satisfy a language-use request.
- When the user explicitly asks for a COBOL or BASIC implementation of a bounded subsystem, implement the smallest coherent utility, document the boundary, add tests/fixtures, and state what remains NOT YET VERIFIED.


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


## Language-aware error repair — 2026-10-06

Recognize the user's A–Z programming-language study list as a **diagnostic/tool-selection reference**, not an instruction to mix every language into the same fix.

- Repair an error in the language/toolchain that owns the failing layer.
- UE5.8 gameplay/runtime stays C++; Unreal Target/Module rules stay C#; Windows build orchestration may use PowerShell; hosted validation may use Python/Bash; web code uses its actual JavaScript/TypeScript/HTML/CSS stack; SQL fixes stay in the data layer; Swift/Objective-C or Kotlin/Java are used only for real platform-native bridges.
- Historical/research/specialized languages (including ActionScript, Ada, ALGOL, APL, Assembly, B, BASIC, BCPL, Brainfuck, Clojure, COBOL, Crystal, D, Delphi/Pascal, Eiffel, Elixir, Elm, Erlang, F#, Factor, Fantom, Fortran, Forth, GML, Groovy, Hack, Haskell, Haxe, Idris, Inform, Io, J, Julia, Koka, Lisp/Scheme, Logo, Lua, MATLAB, ML, Mojo, Nim, Nix, OCaml, Odin, Perl, Prolog, Q, QML, Q#, R, Racket, Raku, Ruby, Scala, Scratch, Smalltalk, Solidity/Yul, Tcl, UnrealScript, V, Vala, VB.NET, XQuery, Zig and others) are used only when an actual owned source/tool/research component requires them. Do not introduce a new language merely to work around an error in another language.
- Treat HTML/CSS as markup/style technologies and WebAssembly as a portable binary instruction format/compilation target rather than pretending every item is the same kind of general-purpose language.
- Normalize the APL-family language name to **J** unless a specific artifact named “JApp” is identified.
- Never infer a root cause from an exit code alone. Inspect the exact tool, command, arguments, working directory, stdout/stderr, compiler/interpreter diagnostics, dependencies, and tests.
- Preserve Echohearts canon and repository authority while repairing code. Never convert a passing static check into a claim of UE5.8 runtime verification.

Canonical language-selection contract: `Dlomotion/Echohearts-Rebearth/09_Technical/LANGUAGE_DIAGNOSTIC_AND_TOOL_SELECTION_STANDARD_2026-10-06.md`.


## Mission-system implementation contract — 2026-10-06

When working on Echohearts missions/quests/objectives:
- use stable `FName MissionId` / `ObjectiveId` as authority; positional/tracking integers are secondary tooling fields only;
- separate immutable mission definitions from mutable runtime progress;
- keep the system event-driven; do not add per-frame Tick polling for mission progression or UMG refresh;
- UE5.8 runtime export macro is `ECHOHEARTS_API`;
- a `UWorldSubsystem` does not replicate by itself: authoritative shared-world state needs a replicated owner/actor/component, and player-private mission state needs a PlayerState/profile-owned lane;
- clients submit intent; they do not directly set Completed or grant rewards;
- dialogue uses typed mission actions rather than parsing arbitrary display text into state changes;
- completion/reward handling must be idempotent and transaction-safe;
- prerequisite unlock evaluation must avoid re-entrant map mutation hazards;
- one gameplay event may progress multiple active missions; do not stop after the first completion unless the authored rule explicitly says so;
- mission examples containing `Blueprint_KinCage` must be corrected to non-coercive safety/field-safehold concepts before canon/runtime promotion;
- do not load DataTable assets with constructor-only helper patterns from subsystem runtime initialization; use an authored asset/data injection path;
- UMG updates are event/delegate driven on the game thread, not background-thread widget mutation.

Canonical contract: `Dlomotion/Echohearts-Rebearth/04_Systems/MISSION_SYSTEM_ARCHITECTURE_2026-10-06.md`.
The mission system is NOT YET UE5.8 VERIFIED and must not bypass the current foundation → Issue #10 → 4–6 Eco-Kin vertical-slice order.

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

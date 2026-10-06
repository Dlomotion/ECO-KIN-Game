---
applyTo: "**"
---

# Echohearts: Rebearth — Cross-Repository Production, Sync, and Code-Repair Protocol

Use this file together with \`.github/copilot-instructions.md\`. It adds repository synchronization, source-control, Unreal, CI, debugging, and code-repair rules. It does not replace canon or repository-specific instructions.

## 1. Repository authority map

Treat these repositories as one production ecosystem with different ownership boundaries, not as seven equal copies:

- \`Dlomotion/Echohearts-Rebearth\` — canonical story, design, systems, production contracts, canon locks, Dex governance, and master project index authority.
- \`Dlomotion/ECHOHEARTS-REBEARTH-BUILD-\` — executable Unreal runtime, build tooling, packaging, CI/runtime evidence, and compiler-driver authority.
- \`Dlomotion/echohearts-web\` — web, presentation, launcher/supporting web application, TypeScript/JavaScript UI, and web-service integration surface.
- \`Dlomotion/Echohearts-Ecokins\` — Eco-Kin specialized support/archive content. It must not create a second Permanent Dex.
- \`Dlomotion/ECO-KIN-Game\` — legacy/prototype support. Reconcile useful code forward; do not let it become a competing production runtime.
- \`Dlomotion/ECHOHEARTS-REBEARTH-\` — legacy Rebearth support. Reconcile useful code/docs toward the canonical and BUILD authorities.
- \`Dlomotion/Echohearts\` — legacy core support. Reconcile useful code/docs toward the canonical and BUILD authorities.

When workspace access includes related repositories, search them before duplicating a subsystem. If cross-repository access is unavailable, state that limitation in the change summary and do not invent the missing repository state.

Never create a second Master Bible, duplicate 125-ID Permanent Dex, duplicate canon tree, duplicate runtime module, duplicate build driver, or parallel implementation authority.

## 2. Canon and mechanics that code must preserve

- Target planet: **Rebearth**.
- Main city: **Echohearts**.
- Creature classification: **Eco-Kin**.
- Player class language: **Frequency Tamer / Core-Binder**.
- Core attributes: **Vibrance, Density, Harmony, Purity**.
- Preserve the **Anima-Link** bi-directional pulse loop for Eco-Kin combat strain/damage and player tactical stamina/health costs.
- Preserve **Huma-Link** for Humanoid-Kin synchronization, social consequence, and tactical strain when the implementation touches Humanoid-Kin systems.
- The Link Device / **A.E.G.I.S.** is the bond interface.
- **Nature** is a Legendary Humanoid-Kin with conditional Mutations. Never call Nature a Legendary Monarch.
- Preserve the 125-ID Permanent Dex as roster authority. Historical names, prototypes, forms, mutations, variants, cosmetics, rename candidates, and retired references must not auto-promote into new species slots.
- Avoid derivative franchise terminology, copied mechanics names, unlicensed assets, and direct mythology imports unless explicitly requested for a technical benchmark. Route contaminated references to redesign/retired documentation rather than making them canon.

## 3. Existing project structure beats duplicate AI-history folders

Do not create a second \`/Docs/AI_Architecture/\` tree merely to store copied chat history.

Use the existing canonical repository structure when the material belongs there:

- \`00_Canon_Lock\`
- \`01_Story\`
- \`02_World\`
- \`03_EcoKin_Dex\`
- \`04_Systems\`
- \`05_Levels\`
- \`06_UI_UX\`
- \`07_Art\`
- \`08_Audio\`
- \`09_Technical\`
- \`10_Production\`
- \`11_Publication\`
- \`99_Reference_Retired_Needs_Redesign\`

Update the existing master index/production index when new authoritative documents are added. Prefer links and concise decision records over duplicating the same design text in several folders.

## 4. Before Copilot creates or fixes code

Perform this order:

1. Identify the current repository and its authority role.
2. Inspect the current branch, relevant folders, existing implementation, call sites, tests, workflows, configuration, \`.uproject\`, \`*.Build.cs\`, \`*.Target.cs\`, and neighboring code as applicable.
3. Read the exact compiler/runtime/CI error before changing code.
4. Search the current repository for an existing subsystem, class, function, interface, data record, or test.
5. Search related Echohearts repositories when access is available and duplication risk is material.
6. Determine the smallest coherent root-cause fix.
7. Preserve public APIs/save formats/network contracts unless a migration is explicitly required.
8. Add or update a test, validator, static check, or reproducible verification step when practical.
9. Run every available local/static/CI check relevant to the change.
10. Report what passed and what still requires Unreal/runtime/hardware evidence.

Do not replace a specific error with a generic workaround. Do not disable required checks, swallow exceptions, comment out failing tests, or fabricate success.

## 5. Language ownership and use

Use the language already owned by the target subsystem.

- **C++**: Unreal gameplay/runtime/modules, reflection-aware systems, replication, engine integrations.
- **Python**: build orchestration, repository validation, asset/data tooling, bounded automation, evidence manifests where appropriate.
- **TypeScript/JavaScript**: \`echohearts-web\` UI, web tools, typed API clients, validation, tests, and web-side automation.
- **C#**: use only when an existing supported tool/service genuinely requires it; do not introduce C# as a replacement for the Unreal C++ runtime.
- **YAML/JSON/INI**: CI, project configuration, data/config contracts where appropriate.

Do not introduce a new language solely because it is available. Prefer strong typing, explicit interfaces, deterministic initialization, bounded input validation, and maintainable tests.

## 6. Unreal Engine target and project detection

Target the active **UE5.8** Echohearts production configuration unless the checked-out repository proves a different migration is underway.

Never hardcode an invented engine path or project file such as \`UE_5.7\` or \`ProjectEngine.uproject\`.

When generating build scripts or workflows:

1. Resolve the actual \`.uproject\` name/path from the repository.
2. Validate the actual Unreal installation/version from the configured runner or environment.
3. Prefer environment variables such as \`UE_ROOT\` and \`UPROJECT_REL\`.
4. Fail early with a useful message when the engine or project file is missing.
5. Use UnrealBuildTool/UnrealHeaderTool through supported Unreal entry points.
6. Do not claim runtime verification if the repository lacks an executable Unreal foundation or the runner lacks Unreal.

Keep the runtime module name \`Echohearts\` and export macro \`ECHOHEARTS_API\` unless an explicit, repository-wide migration is approved.

For Unreal C++:
- keep \`.generated.h\` in the valid include position;
- keep declaration/definition signatures synchronized;
- use valid \`UCLASS\`, \`USTRUCT\`, \`UENUM\`, \`UINTERFACE\`, \`UPROPERTY\`, and \`UFUNCTION\` syntax;
- never invent Unreal APIs, metadata specifiers, replication flags, engine modules, or RPC behavior;
- use server-authoritative multiplayer logic and treat client input as untrusted;
- validate authority, ownership, finite numeric values, bounds, legal state transitions, rate limits, inventory/resources, placement/collision, and permissions;
- avoid uncontrolled Tick when events, timers, StateTree/Behavior Tree/Mass, or bounded tasks are more appropriate.

## 7. Git repository protocol

If the repository is already cloned, **do not run \`git init\`** inside it.

Prefer:

\`\`\`bash
git switch main
git pull --ff-only
git lfs install
git switch -c <type>/<short-description>
\`\`\`

Use feature/fix/chore branches for code, build, workflow, and risky documentation changes. Prefer pull requests into \`main\`.

Before committing:

\`\`\`text
edit
→ build/lint/test
→ inspect errors
→ fix root cause
→ rerun checks
→ git diff
→ stage only intended files
→ commit
→ push feature branch
→ pull request
→ CI/review
→ merge
\`\`\`

Do not commit merely because a build command started. Do not mix unrelated generated files into a fix.

## 8. Unreal \`.gitignore\` policy

Ignore generated/build-cache material while preserving authored project resources.

Recommended baseline when these paths exist:

\`\`\`gitignore
Binaries/
DerivedDataCache/
Intermediate/
Saved/
LocalBuilds/
StagedBuilds/

Plugins/**/Binaries/
Plugins/**/Intermediate/

.vs/
.idea/
*.sln
*.suo
*.opensdf
*.sdf
*.VC.db
*.VC.VC.opendb

*.pdb
*.obj
*.ipch

.DS_Store
Thumbs.db
Desktop.ini
\`\`\`

Do **not** blindly ignore all of \`Build/\`; Unreal projects can contain required icons, receipts/resources, platform files, or authored build inputs there.

Do **not** ignore \`Content/\`.

When changing \`.gitignore\`, inspect the repository first so required existing files are not orphaned.

## 9. Git LFS policy

Use Git LFS for Unreal binary assets and large source assets. Typical patterns:

\`\`\`gitattributes
*.uasset filter=lfs diff=lfs merge=lfs -text
*.umap   filter=lfs diff=lfs merge=lfs -text
*.fbx    filter=lfs diff=lfs merge=lfs -text
*.blend  filter=lfs diff=lfs merge=lfs -text
*.psd    filter=lfs diff=lfs merge=lfs -text
*.tga    filter=lfs diff=lfs merge=lfs -text
*.exr    filter=lfs diff=lfs merge=lfs -text
*.wav    filter=lfs diff=lfs merge=lfs -text
*.flac   filter=lfs diff=lfs merge=lfs -text
*.mp4    filter=lfs diff=lfs merge=lfs -text
\`\`\`

Do not automatically put every \`.png\` into LFS. Small UI/documentation images can remain normal Git files; large production art can be added to LFS according to repository policy.

Never rewrite existing LFS history, migrate large historical assets, or force-push rewritten history without explicit approval and a rollback plan.

After checkout on a build machine, ensure LFS objects are available before compiling/cooking.

## 10. Branch rules and required checks

The intended production policy for \`main\` is:

- protect the default branch;
- restrict deletion;
- block force pushes;
- require pull requests for changes to protected production code;
- require conversation resolution where practical;
- keep an emergency owner/admin bypass narrowly available;
- require status checks only when those checks are guaranteed to run for the affected pull request.

Do not target every feature branch with the same strict production rules unless explicitly requested.

Do not make a path-limited workflow a universal required check. For example, a workflow that runs only when \`09_Technical/MetaSystems/**\` changes cannot safely be the sole mandatory status check for unrelated documentation/art/web pull requests.

Create an always-running lightweight PR gate first if a repository needs a universal required status.

## 11. CI and self-hosted Unreal runner safety

For Unreal Windows packaging/build jobs:

- prefer a trusted, labeled self-hosted Windows runner with the required UE5.8 toolchain;
- use \`actions/checkout\` with LFS enabled and explicitly verify LFS state;
- validate \`UE_ROOT\` and \`UPROJECT_REL\` before invoking UBT/UAT;
- start with Development build/package evidence before treating Shipping as the default proof path;
- retain useful logs and artifact metadata;
- do not hardcode a local user's machine path when an environment variable is appropriate.

For a **public repository**, do not automatically execute untrusted fork pull-request code on a personal/self-hosted machine. Use a trusted-branch trigger, explicit approval boundary, or \`workflow_dispatch\`/controlled workflow design until runner isolation is proven.

A CI process exit code is tool-specific. **Exit code 2 does not have one universal meaning.** Read the failing command, tool, arguments, working directory, stdout, stderr, and the first actionable diagnostic before editing code.

## 12. Unreal editor/build loop

Closing Unreal Editor is required for some structural changes, not every edit.

Close/restart the editor for changes such as:
- module/target/build-rule changes;
- plugin enablement or plugin module changes;
- structural reflected-type changes when live coding/hot reload is unsafe;
- locked asset/module state;
- full clean rebuilds.

Normal bounded iteration can use the supported editor/live-coding workflow when the change is safe for it.

Preferred evidence progression:

\`\`\`text
static/repository validation
→ LFS verification
→ UHT/Development Editor compile
→ editor launch
→ authored minimal map load
→ PIE
→ bounded automation
→ Development package
→ packaged launch
→ multiplayer/save/platform-specific validation
\`\`\`

Do not label a system VERIFIED before the evidence required for that system actually exists.

## 13. Debugging and code-fix behavior

When an error is reported:

1. Preserve the exact first actionable error and nearby context.
2. Reproduce on the smallest reliable command/test.
3. Separate primary errors from cascading failures.
4. Inspect includes, generated-code/reflection requirements, module dependencies, target rules, file casing, path assumptions, asset references, serialization versioning, and network authority as relevant.
5. Fix the root cause, not only the final symptom.
6. Add a regression check when practical.
7. Rerun the same failing command before broadening the test scope.
8. Only then run wider CI/build/runtime verification.

Never infer that a missing module, missing asset, class name, or manager exists merely because a prompt mentioned it. For example, do not assume \`UGlobalAudioPoolManager\` exists; search for it first. If it does not exist, create it only when the requested design requires a new audio-pooling subsystem and the owning repository is clear.

Likewise, shader/glitch-wireframe material work must use actual project material parameters/assets rather than invented graph nodes.

## 14. Secure code-generation rules

- Never commit secrets, tokens, passwords, private keys, runner credentials, cloud credentials, or local absolute paths.
- Use environment variables/secrets stores for credentials.
- Treat network/client payloads and save imports as untrusted.
- Bound arrays, sizes, indexes, timers, retries, rates, coordinates, and numeric values.
- Validate serialization versions before migration.
- Keep background work thread-safe and avoid unsafe UObject mutation off the game thread.
- Prefer deterministic state transitions and explicit failure paths.
- Preserve cloud-save/profile registry integrity and versioning.
- Keep cross-platform behavior explicit rather than assuming Windows-only semantics in shared runtime code.

## 15. GitHub/public-code lookup behavior

When looking for a fix:

1. Search the current repository and related Echohearts repositories first.
2. Search authoritative engine documentation/issues or public code only when needed.
3. Understand the license, engine version, and context of any external example.
4. Do not paste third-party code blindly.
5. Adapt the underlying technique to Echohearts architecture and write project-native tests.
6. Never convert an external workaround into canon terminology or a permanent subsystem without design review.

## 16. Verification vocabulary

Use these labels precisely:

- **STATIC CHECK PASSED**
- **REPOSITORY CONTRACT PASSED**
- **CI PREFLIGHT PASSED**
- **NOT VERIFIED — UE BUILD/RUNTIME EVIDENCE REQUIRED**

Do not claim **compiled**, **fixed**, **production-ready**, **optimized**, **secure**, or **VERIFIED** unless the required evidence was actually produced.

A successful shell/Python/static command proves only that command. It does not prove UHT, editor startup, gameplay, save/load, networking, AI, packaging, cross-play, hardware behavior, or performance.

## 17. Required Copilot outcome

When asked to create or repair code, do not stop at generic advice.

Inspect the repository, identify the owning subsystem, implement the smallest correct change, preserve Echohearts canon/contracts, update tests or validation, run the checks available in the environment, and provide a concise summary containing:

- files changed;
- root cause or requested implementation;
- tests/checks run;
- what passed;
- what still requires runtime/UE/hardware verification;
- any cross-repository follow-up that cannot be completed from the current workspace.

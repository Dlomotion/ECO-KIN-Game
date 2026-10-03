using UnrealBuildTool;
public class EchoheartsRebearth : ModuleRules
{
    public EchoheartsRebearth(ReadOnlyTargetRules Target) : base(Target)
    {
        PCHUsage = PCHUsageMode.UseExplicitOrSharedPCHs;
        PublicDependencyModuleNames.AddRange(new[] { "Core", "CoreUObject", "Engine", "NetCore" });
    }
}

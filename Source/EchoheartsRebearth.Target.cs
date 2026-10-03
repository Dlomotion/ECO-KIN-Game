using UnrealBuildTool;
public class EchoheartsRebearthTarget : TargetRules
{
    public EchoheartsRebearthTarget(TargetInfo Target) : base(Target)
    {
        Type = TargetType.Game;
        DefaultBuildSettings = BuildSettingsVersion.Latest;
        IncludeOrderVersion = EngineIncludeOrderVersion.Latest;
        ExtraModuleNames.Add("EchoheartsRebearth");
    }
}

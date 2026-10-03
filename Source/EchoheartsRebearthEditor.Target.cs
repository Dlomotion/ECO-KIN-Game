using UnrealBuildTool;
public class EchoheartsRebearthEditorTarget : TargetRules
{
    public EchoheartsRebearthEditorTarget(TargetInfo Target) : base(Target)
    {
        Type = TargetType.Editor;
        DefaultBuildSettings = BuildSettingsVersion.Latest;
        IncludeOrderVersion = EngineIncludeOrderVersion.Latest;
        ExtraModuleNames.Add("EchoheartsRebearth");
    }
}

// Optional Unity prototype DTO. NOT a second authoritative game server.
// Unity C# project integration and compilation are NOT VERIFIED.
using System;
namespace Echohearts.Rebearth.Prototype
{
    [Serializable]
    public struct EcoKinAttributes
    {
        public float Vibrance;
        public float Density;
        public float Harmony;
        public float Purity;
    }

    [Serializable]
    public sealed class RebearthDomainSnapshot
    {
        public int SchemaVersion = 1;
        public string CanonicalDomainId = "";
        public string CanonicalRegionId = "";
        public EcoKinAttributes Ecology;
        public int RestorationProjects;
        public bool AquaticHabitatRestored;
        public bool CrossingSupplied;
    }

    // Deserialize a server-approved snapshot; never use client data to grant quest completion.
    public static class RebearthSnapshotValidation
    {
        public static bool IsSane(RebearthDomainSnapshot state)
        {
            if (state == null || state.SchemaVersion != 1 || string.IsNullOrWhiteSpace(state.CanonicalDomainId))
                return false;
            return InRange(state.Ecology.Vibrance) && InRange(state.Ecology.Density)
                && InRange(state.Ecology.Harmony) && InRange(state.Ecology.Purity)
                && state.RestorationProjects >= 0;
        }
        private static bool InRange(float x) => !float.IsNaN(x) && !float.IsInfinity(x) && x >= 0f && x <= 100f;
    }
}

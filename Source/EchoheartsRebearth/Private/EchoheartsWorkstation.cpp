#include "EchoheartsWorkstation.h"
#include "Components/SceneComponent.h"
#include "Net/UnrealNetwork.h"

AEchoheartsWorkstation::AEchoheartsWorkstation()
{
    PrimaryActorTick.bCanEverTick = true;
    bReplicates = true;
    SetRootComponent(CreateDefaultSubobject<USceneComponent>(TEXT("Root")));
}
void AEchoheartsWorkstation::Tick(float DeltaSeconds)
{
    Super::Tick(DeltaSeconds);
    if (HasAuthority() && bWorkerAssigned && FMath::IsFinite(DeltaSeconds) && DeltaSeconds > 0 &&
        FMath::IsFinite(YieldPerSecond) && YieldPerSecond > 0)
    {
        StoredYield = FMath::Min(StoredYield + YieldPerSecond * DeltaSeconds, 1000000.0f);
    }
}
void AEchoheartsWorkstation::SetWorkerAssigned(bool bAssigned)
{
    if (HasAuthority()) { bWorkerAssigned = bAssigned; ForceNetUpdate(); }
}
void AEchoheartsWorkstation::GetLifetimeReplicatedProps(TArray<FLifetimeProperty>& OutLifetimeProps) const
{
    Super::GetLifetimeReplicatedProps(OutLifetimeProps);
    DOREPLIFETIME(AEchoheartsWorkstation, bWorkerAssigned);
    DOREPLIFETIME(AEchoheartsWorkstation, StoredYield);
}

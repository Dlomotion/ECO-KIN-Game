#pragma once
#include "CoreMinimal.h"
#include "GameFramework/Actor.h"
#include "EchoheartsWorkstation.generated.h"

UCLASS(Blueprintable)
class ECHOHEARTSREBEARTH_API AEchoheartsWorkstation : public AActor
{
    GENERATED_BODY()
public:
    AEchoheartsWorkstation();
    virtual void Tick(float DeltaSeconds) override;
    virtual void GetLifetimeReplicatedProps(TArray<FLifetimeProperty>& OutLifetimeProps) const override;

    UPROPERTY(EditAnywhere, BlueprintReadWrite, Category="Workstation", meta=(ClampMin="0"))
    float YieldPerSecond = 5.0f;
    UPROPERTY(Replicated, BlueprintReadOnly, Category="Workstation")
    bool bWorkerAssigned = false;
    UPROPERTY(Replicated, BlueprintReadOnly, Category="Workstation")
    float StoredYield = 0.0f;

    // Invoke on the server after validating worker ownership and availability.
    UFUNCTION(BlueprintCallable, BlueprintAuthorityOnly, Category="Workstation")
    void SetWorkerAssigned(bool bAssigned);
};

#pragma once
#include "CoreMinimal.h"
#include "EchoheartsNetworkPayload.generated.h"

UENUM(BlueprintType)
enum class EEchoInventoryAction : uint8 { Extract, Craft, Use };

 // Intent only: the server resolves recipes, damage, inventory and actor ownership.
USTRUCT(BlueprintType)
struct ECHOHEARTSREBEARTH_API FEchoInventoryIntent
{
    GENERATED_BODY()
    UPROPERTY() uint32 Sequence = 0;
    UPROPERTY() EEchoInventoryAction Action = EEchoInventoryAction::Extract;
    UPROPERTY() uint16 ItemCode = 0;
    UPROPERTY() uint16 Quantity = 1;
    UPROPERTY() uint32 TargetId = 0;

    bool IsValid() const
    {
        return static_cast<uint8>(Action) <= static_cast<uint8>(EEchoInventoryAction::Use)
            && ItemCode != 0 && Quantity > 0 && Quantity <= 999;
    }
    bool NetSerialize(FArchive& Ar, UPackageMap* Map, bool& bOutSuccess)
    {
        uint8 ActionByte = static_cast<uint8>(Action);
        Ar << Sequence;
        Ar.SerializeBits(&ActionByte, 2);
        Ar << ItemCode << Quantity << TargetId;
        if (Ar.IsLoading()) { Action = static_cast<EEchoInventoryAction>(ActionByte); }
        bOutSuccess = !Ar.IsError() && IsValid();
        return true;
    }
};
template<> struct TStructOpsTypeTraits<FEchoInventoryIntent> : TStructOpsTypeTraitsBase2<FEchoInventoryIntent>
{
    enum { WithNetSerializer = true };
};

def solve(
    total_weight_needed: int = 1000, # needs to gain 1000 pounds
    weight_from_berries_fraction: float = 1/5, # gained a fifth of the weight it needed from berries
    weight_from_acorns_multiplier: int = 2, # gained twice that amount from acorns
    weight_from_salmon_fraction: float = 1/2 # Salmon made up half of the remaining weight
):
    """Index: 61.
    Returns: the number of pounds the bear gained eating small animals.
    """
    #: L1
    weight_from_berries = total_weight_needed * weight_from_berries_fraction

    #: L2
    weight_from_acorns = weight_from_berries * weight_from_acorns_multiplier

    #: L3
    remaining_weight_needed = total_weight_needed - weight_from_berries - weight_from_acorns

    #: L4
    weight_from_salmon = remaining_weight_needed * weight_from_salmon_fraction

    #: L5
    weight_from_small_animals = remaining_weight_needed - weight_from_salmon

    answer = weight_from_small_animals # FINAL ANSWER
    return answer
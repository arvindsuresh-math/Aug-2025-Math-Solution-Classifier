def solve(
    weight_needed: int = 1000, # needs to gain 1000 pounds
    fraction_from_berries: float = 1/5, # gained a fifth of the weight it needed from berries
    multiplier_acorns: int = 2, # gained twice that amount from acorns
    fraction_from_salmon: float = 1/2 # Salmon made up half of the remaining weight it had needed to gain
):
    """Index: 61.
    Returns: the number of pounds the bear gained eating small animals.
    """
    #: L1
    weight_from_berries = fraction_from_berries * weight_needed

    #: L2
    weight_from_acorns = multiplier_acorns * weight_from_berries

    #: L3
    remaining_weight_needed = weight_needed - weight_from_berries - weight_from_acorns

    #: L4
    weight_from_salmon = remaining_weight_needed * fraction_from_salmon

    #: L5
    weight_from_small_animals = remaining_weight_needed - weight_from_salmon

    answer = weight_from_small_animals # FINAL ANSWER
    return answer
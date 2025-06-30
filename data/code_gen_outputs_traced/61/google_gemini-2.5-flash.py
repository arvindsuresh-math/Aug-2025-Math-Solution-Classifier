def solve(
        weight_needed_total: int = 1000, # needs to gain 1000 pounds
        fraction_from_berries: float = 1/5, # gained a fifth of the weight it needed from berries
        multiplier_acorns: int = 2, # gained twice that amount from acorns
        fraction_from_salmon: float = 1/2 # Salmon made up half of the remaining weight
    ):
    """Index: 61.
    Returns: the number of pounds the bear gained eating small animals.
    """
    #: L1
    weight_from_berries = weight_needed_total * fraction_from_berries # eval: 200.0 = 1000 * 0.2
    #: L2
    weight_from_acorns = multiplier_acorns * weight_from_berries # eval: 400.0 = 2 * 200.0
    #: L3
    remaining_weight_after_berries_acorns = weight_needed_total - weight_from_berries - weight_from_acorns # eval: 400.0 = 1000 - 200.0 - 400.0
    #: L4
    weight_from_salmon = remaining_weight_after_berries_acorns * fraction_from_salmon # eval: 200.0 = 400.0 * 0.5
    #: L5
    weight_from_small_animals = remaining_weight_after_berries_acorns - weight_from_salmon # eval: 200.0 = 400.0 - 200.0
    answer = weight_from_small_animals # FINAL ANSWER # eval: 200.0 = 200.0 # FINAL ANSWER
    return answer # eval: return 200.0
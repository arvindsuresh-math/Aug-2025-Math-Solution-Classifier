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
    weight_from_berries = 210.0 # eval: 210.0 = 210.0

    #: L2
    weight_from_acorns = multiplier_acorns * weight_from_berries # eval: 420.0 = 2 * 210.0

    #: L3
    remaining_weight_after_berries_acorns = weight_needed_total - weight_from_berries - weight_from_acorns # eval: 370.0 = 1000 - 210.0 - 420.0

    #: L4
    weight_from_salmon = remaining_weight_after_berries_acorns * fraction_from_salmon # eval: 185.0 = 370.0 * 0.5

    #: L5
    weight_from_small_animals = remaining_weight_after_berries_acorns - weight_from_salmon # eval: 185.0 = 370.0 - 185.0

    #: FA
    answer = weight_from_small_animals
    return answer # eval: return 185.0

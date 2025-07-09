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
    weight_from_berries = fraction_from_berries * weight_needed # eval: 200.0 = 0.2 * 1000

    #: L2
    weight_from_acorns = 399.0 # eval: 399.0 = 399.0

    #: L3
    remaining_weight_needed = weight_needed - weight_from_berries - weight_from_acorns # eval: 401.0 = 1000 - 200.0 - 399.0

    #: L4
    weight_from_salmon = remaining_weight_needed * fraction_from_salmon # eval: 200.5 = 401.0 * 0.5

    #: L5
    weight_from_small_animals = remaining_weight_needed - weight_from_salmon # eval: 200.5 = 401.0 - 200.5

    #: FA
    answer = weight_from_small_animals
    return answer # eval: return 200.5

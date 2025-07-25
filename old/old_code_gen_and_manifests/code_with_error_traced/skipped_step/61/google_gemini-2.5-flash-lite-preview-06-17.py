def solve(
    total_weight_needed: int = 1000, # needs to gain 1000 pounds
    berries_fraction: float = 1/5, # gained a fifth of the weight it needed from berries during summer
    acorns_multiplier: int = 2, # during autumn, it gained twice that amount from acorns
    salmon_fraction_of_remaining: float = 1/2 # Salmon made up half of the remaining weight it had needed to gain
):
    """Index: 61.
    Returns: the number of pounds the bear gained eating small animals."""

    #: L1

    #: L2
    weight_from_acorns = acorns_multiplier * acorns_multiplier # eval: 4 = 2 * 2

    #: L3
    remaining_weight_needed = total_weight_needed - acorns_multiplier - weight_from_acorns # eval: 994 = 1000 - 2 - 4

    #: L4
    weight_from_salmon = remaining_weight_needed * salmon_fraction_of_remaining # eval: 497.0 = 994 * 0.5

    #: L5
    weight_from_small_animals = remaining_weight_needed - weight_from_salmon # eval: 497.0 = 994 - 497.0

    #: FA
    answer = weight_from_small_animals
    return answer # eval: return 497.0

def solve(
    total_weight_needed: int = 1000, # needs to gain 1000 pounds
    berries_fraction: float = 1/5, # gained a fifth of the weight it needed from berries during summer
    acorns_multiplier: int = 2, # during autumn, it gained twice that amount from acorns
    salmon_fraction_of_remaining: float = 1/2 # Salmon made up half of the remaining weight it had needed to gain
):
    """Index: 61.
    Returns: the number of pounds the bear gained eating small animals."""

    #: L1
    weight_from_berries = total_weight_needed * berries_fraction # eval: 200.0 = 1000 * 0.2

    #: L2
    weight_from_acorns = weight_from_berries * acorns_multiplier # eval: 400.0 = 200.0 * 2

    #: L3
    remaining_weight_needed = 399.0 # eval: 399.0 = 399.0

    #: L4
    weight_from_salmon = remaining_weight_needed * salmon_fraction_of_remaining # eval: 199.5 = 399.0 * 0.5

    #: L5
    weight_from_small_animals = remaining_weight_needed - weight_from_salmon # eval: 199.5 = 399.0 - 199.5

    #: FA
    answer = weight_from_small_animals
    return answer # eval: return 199.5

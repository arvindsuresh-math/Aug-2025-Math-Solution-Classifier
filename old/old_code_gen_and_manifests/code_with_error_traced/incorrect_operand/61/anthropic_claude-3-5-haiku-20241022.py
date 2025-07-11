def solve(
    total_weight_needed: int = 1000,  # bear needs to gain 1000 pounds
    berry_fraction: float = 1/5,  # gained a fifth of the weight from berries
    acorn_multiplier: int = 2,  # gained twice the berry amount from acorns
    salmon_fraction: float = 1/2  # salmon made up half of the remaining weight
):
    """Index: 61.
    Returns: the number of pounds the bear gained from eating small animals."""

    #: L1
    berry_weight = berry_fraction * acorn_multiplier # eval: 0.4 = 0.2 * 2

    #: L2
    acorn_weight = acorn_multiplier * berry_weight # eval: 0.8 = 2 * 0.4

    #: L3
    remaining_weight = total_weight_needed - berry_weight - acorn_weight # eval: 998.8000000000001 = 1000 - 0.4 - 0.8

    #: L4
    salmon_weight = remaining_weight * salmon_fraction # eval: 499.40000000000003 = 998.8000000000001 * 0.5

    #: L5
    small_animals_weight = remaining_weight - salmon_weight # eval: 499.40000000000003 = 998.8000000000001 - 499.40000000000003

    #: FA
    answer = small_animals_weight
    return answer # eval: return 499.40000000000003

def solve(
    total_weight_needed: int = 1000,  # bear needs to gain 1000 pounds
    berry_fraction: float = 1/5,  # gained a fifth of the weight from berries
    acorn_multiplier: int = 2,  # gained twice the berry amount from acorns
    salmon_fraction: float = 1/2  # salmon made up half of the remaining weight
):
    """Index: 61.
    Returns: the number of pounds the bear gained from eating small animals."""

    #: L1
    berry_weight = berry_fraction * total_weight_needed # eval: 200.0 = 0.2 * 1000

    #: L2
    acorn_weight = acorn_multiplier * berry_weight # eval: 400.0 = 2 * 200.0

    #: L3
    remaining_weight = total_weight_needed - berry_weight - acorn_weight # eval: 400.0 = 1000 - 200.0 - 400.0

    #: L4
    salmon_weight = remaining_weight * salmon_fraction # eval: 200.0 = 400.0 * 0.5

    #: L5
    small_animals_weight = remaining_weight - salmon_weight # eval: 200.0 = 400.0 - 200.0

    #: FA
    answer = small_animals_weight
    return answer # eval: return 200.0

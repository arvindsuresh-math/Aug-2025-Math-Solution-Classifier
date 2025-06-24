def solve(
    total_weight_needed: int = 1000,  # bear needs to gain 1000 pounds
    berry_fraction: float = 1/5,  # gained a fifth of the weight from berries
    acorn_multiplier: int = 2,  # gained twice the berry amount from acorns
    salmon_fraction: float = 1/2  # salmon made up half of the remaining weight
):
    """Index: 61.
    Returns: the number of pounds the bear gained from eating small animals."""
    
    #: L1
    berry_weight = berry_fraction * total_weight_needed

    #: L2
    acorn_weight = acorn_multiplier * berry_weight

    #: L3
    remaining_weight = total_weight_needed - berry_weight - acorn_weight

    #: L4
    salmon_weight = remaining_weight * salmon_fraction

    #: L5
    small_animals_weight = remaining_weight - salmon_weight

    answer = small_animals_weight  # FINAL ANSWER
    return answer
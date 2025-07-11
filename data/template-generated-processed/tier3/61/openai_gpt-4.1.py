from fractions import Fraction

def solve():
    """Index: 61.
    Returns: the number of pounds the bear gained eating small animals.
    """
    # L1
    total_needed = 1000 # needs to gain 1000 pounds
    berries_fraction = Fraction(1, 5) # gained a fifth of the weight from berries
    berries_gain = berries_fraction * total_needed

    # L2
    acorns_multiplier = 2 # gained twice that amount from acorns
    acorns_gain = acorns_multiplier * berries_gain

    # L3
    remaining_after_berries_acorns = total_needed - berries_gain - acorns_gain

    # L4
    salmon_divisor = 2 # salmon made up half of the remaining weight
    salmon_gain = remaining_after_berries_acorns / salmon_divisor

    # L5
    small_animals_gain = remaining_after_berries_acorns - salmon_gain

    # FA
    answer = small_animals_gain
    return answer
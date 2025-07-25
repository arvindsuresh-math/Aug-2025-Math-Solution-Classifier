from fractions import Fraction

def solve():
    """Index: 5587.
    Returns: the total number of apples remaining.
    """
    # L1
    blue_apples = 5 # 5 blue apples
    yellow_multiplier = 2 # twice as many yellow apples
    yellow_apples = blue_apples * yellow_multiplier

    # L2
    total_apples_before_giving = yellow_apples + blue_apples

    # L3
    fraction_given_to_son = Fraction(1, 5) # 1/5 of the total number of apples
    apples_given_to_son = fraction_given_to_son * total_apples_before_giving

    # L4
    remaining_apples = total_apples_before_giving - apples_given_to_son

    # FA
    answer = remaining_apples
    return answer
from fractions import Fraction

def solve():
    """Index: 6377.
    Returns: the total number of apples remaining in the tree.
    """
    # L1
    first_day_fraction = Fraction(1, 5) # 1/5 of the fruits
    total_apples = 200 # grew 200 apples
    apples_picked_first_day = first_day_fraction * total_apples

    # L2
    second_day_multiplier = 2 # twice that number
    apples_picked_second_day = second_day_multiplier * apples_picked_first_day

    # L3
    additional_apples_third_day = 20 # 20 more apples than he picked on the first day
    apples_picked_third_day = apples_picked_first_day + additional_apples_third_day

    # L4
    total_apples_picked = apples_picked_first_day + apples_picked_second_day + apples_picked_third_day

    # L5
    apples_remaining = total_apples - total_apples_picked

    # FA
    answer = apples_remaining
    return answer
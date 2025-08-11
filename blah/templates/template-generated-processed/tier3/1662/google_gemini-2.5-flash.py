from fractions import Fraction

def solve():
    """Index: 1662.
    Returns: the total number of fruits remaining on the tomato plant.
    """
    # L1
    first_pick_fraction = Fraction(1, 4) # 1/4 of that number
    initial_tomatoes = 100 # A tomato plant has 100 tomatoes
    first_pick_amount = first_pick_fraction * initial_tomatoes

    # L2
    remaining_after_first_pick = initial_tomatoes - first_pick_amount

    # L3
    second_pick_amount = 20 # picks 20 more tomatoes
    remaining_after_second_pick = remaining_after_first_pick - second_pick_amount

    # L4
    twice_factor = 2 # twice that number
    third_pick_amount = second_pick_amount * twice_factor

    # L5
    final_remaining_tomatoes = remaining_after_second_pick - third_pick_amount

    # FA
    answer = final_remaining_tomatoes
    return answer
from fractions import Fraction

def solve():
    """Index: 4169.
    Returns: the total number of plums and apples remaining on the trees.
    """
    # L1
    initial_apples = 180 # 180 apples on the apple tree
    apple_to_plum_ratio = 3 # three times as many apples as the number of plums
    initial_plums = initial_apples // apple_to_plum_ratio

    # L2
    fraction_picked = Fraction(3, 5) # 3/5 of the fruits
    picked_apples = fraction_picked * initial_apples

    # L3
    remaining_apples = initial_apples - picked_apples

    # L4
    picked_plums = fraction_picked * initial_plums

    # L5
    remaining_plums = initial_plums - picked_plums

    # L6
    total_remaining_fruits = remaining_apples + remaining_plums

    # FA
    answer = total_remaining_fruits
    return answer
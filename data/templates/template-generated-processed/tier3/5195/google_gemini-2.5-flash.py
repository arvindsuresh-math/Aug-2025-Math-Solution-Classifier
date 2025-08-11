from fractions import Fraction

def solve():
    """Index: 5195.
    Returns: the number of burger slices left for Era.
    """
    # L1
    num_burgers = 5 # 5 burgers
    half_unit = Fraction(1, 2) # sliced each burger into halves
    total_slices = num_burgers / half_unit

    # L2
    first_friend_slices = 1 # The first and second friends got 1 and 2 slices
    second_friend_slices = 2 # The first and second friends got 1 and 2 slices
    first_two_friends_slices = first_friend_slices + second_friend_slices

    # L3
    third_friend_slices = 3 # Then the third and fourth friends got 3 slices each
    fourth_friend_slices = 3 # Then the third and fourth friends got 3 slices each
    third_fourth_friends_slices = third_friend_slices + fourth_friend_slices

    # L4
    total_friends_slices = first_two_friends_slices + third_fourth_friends_slices

    # L5
    era_remaining_slices = total_slices - total_friends_slices

    # FA
    answer = era_remaining_slices
    return answer
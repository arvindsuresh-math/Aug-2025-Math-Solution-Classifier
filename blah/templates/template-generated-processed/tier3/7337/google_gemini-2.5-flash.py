from fractions import Fraction

def solve():
    """Index: 7337.
    Returns: the total number of road signs at the four intersections.
    """
    # L1
    fraction_more_signs = Fraction(1, 4) # 1/4 times more road signs
    signs_at_first_intersection = 40 # 40 road signs
    additional_signs_second_intersection = fraction_more_signs * signs_at_first_intersection

    # L2
    signs_at_second_intersection = signs_at_first_intersection + additional_signs_second_intersection

    # L3
    total_signs_first_two = signs_at_second_intersection + signs_at_first_intersection

    # L4
    multiplier_third_intersection = 2 # twice the number
    signs_at_third_intersection = multiplier_third_intersection * signs_at_second_intersection

    # L5
    total_signs_first_three = total_signs_first_two + signs_at_third_intersection

    # L6
    fewer_signs_fourth_intersection = 20 # 20 fewer than those at the third intersection
    signs_at_fourth_intersection = signs_at_third_intersection - fewer_signs_fourth_intersection

    # L7
    total_signs_all_four = total_signs_first_three + signs_at_fourth_intersection

    # FA
    answer = total_signs_all_four
    return answer
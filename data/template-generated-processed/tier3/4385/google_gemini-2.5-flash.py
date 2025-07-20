from fractions import Fraction

def solve():
    """Index: 4385.
    Returns: 2/3 of the difference between the number of black and white scores used.
    """
    # L1
    white_ratio_part = 7 # ratio of 7:6
    black_ratio_part = 6 # ratio of 7:6
    total_ratio_parts = white_ratio_part + black_ratio_part

    # L2
    ratio_part_difference = white_ratio_part - black_ratio_part

    # L3
    total_yellow_scores = 78 # 78 yellow scores
    difference_in_scores = Fraction(ratio_part_difference, total_ratio_parts) * total_yellow_scores

    # L4
    fraction_multiplier_numerator = 2 # 2/3 of the difference
    fraction_multiplier_denominator = 3 # 2/3 of the difference
    final_answer_value = Fraction(fraction_multiplier_numerator, fraction_multiplier_denominator) * difference_in_scores

    # FA
    answer = final_answer_value
    return answer
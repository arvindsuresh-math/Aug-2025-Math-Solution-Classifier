def solve():
    """Index: 1909.
    Returns: the number of kids who take more than 14 minutes.
    """
    # L1
    total_kids = 40 # 40 kids are running a race
    percent_under_6_min_num = 10 # 10% of them
    percent_factor = 0.01 # WK
    kids_under_6_min = total_kids * percent_under_6_min_num * percent_factor

    # L2
    multiplier_for_8_min = 3 # Three times that number
    kids_under_8_min = kids_under_6_min * multiplier_for_8_min

    # L3
    remaining_kids = total_kids - kids_under_6_min - kids_under_8_min

    # L4
    divisor_for_14_min = 6 # 1/6 of the remaining kids
    kids_more_than_14_min = remaining_kids / divisor_for_14_min

    # FA
    answer = kids_more_than_14_min
    return answer
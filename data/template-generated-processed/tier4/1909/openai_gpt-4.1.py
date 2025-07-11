def solve():
    """Index: 1909.
    Returns: the number of kids who take more than 14 minutes.
    """
    # L1
    total_kids = 40 # 40 kids are running a race
    percent_under_6 = 10 # 10% of them pass the finish line in less than 6 minutes
    percent_factor = 0.01 # WK
    kids_under_6 = total_kids * percent_under_6 * percent_factor

    # L2
    triple_factor = 3 # Three times that number finish in less than 8 minutes
    kids_under_8 = kids_under_6 * triple_factor

    # L3
    kids_remaining = total_kids - kids_under_6 - kids_under_8

    # L4
    divisor_over_14 = 6 # 1/6 of the remaining kids take more than 14 minutes
    kids_over_14 = kids_remaining / divisor_over_14

    # FA
    answer = kids_over_14
    return answer
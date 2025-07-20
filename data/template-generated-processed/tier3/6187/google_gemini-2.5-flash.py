def solve():
    """Index: 6187.
    Returns: the Dow Jones Industrial Average before the markets opened.
    """
    # L1
    dow_end_of_day = 8722 # The Dow ended the day at 8,722
    fall_percentage = 2 # fell 2%
    remaining_percentage_basis = 98 # WK (100% - 2% fall)
    dow_fall_amount = dow_end_of_day / remaining_percentage_basis * fall_percentage

    # L2
    dow_start_of_day = dow_end_of_day + dow_fall_amount

    # FA
    answer = dow_start_of_day
    return answer
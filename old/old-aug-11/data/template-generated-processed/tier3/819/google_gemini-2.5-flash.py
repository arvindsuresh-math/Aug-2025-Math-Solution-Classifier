def solve():
    """Index: 819.
    Returns: the number of tins collected each day for the rest of the week.
    """
    # L1
    first_day_tins = 50 # On the first day, he collects 50 tins
    multiplier = 3 # 3 times that number
    second_day_tins = multiplier * first_day_tins

    # L2
    fewer_tins = 50 # 50 tins fewer
    third_day_tins = second_day_tins - fewer_tins

    # L3
    total_three_days = second_day_tins + third_day_tins + first_day_tins

    # L4
    weekly_goal = 500 # collecting 500 tins in a week
    tins_needed = weekly_goal - total_three_days

    # L5
    remaining_days = 4 # total number of days left in the week is 4
    tins_per_day_remaining = tins_needed / remaining_days

    # FA
    answer = tins_per_day_remaining
    return answer
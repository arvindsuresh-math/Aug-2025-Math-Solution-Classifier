def solve():
    """Index: 6478.
    Returns: the total height of the corn plants.
    """
    # L1
    first_week_growth = 2 # grown 2 inches
    multiplier_twice = 2 # WK
    second_week_growth = multiplier_twice * first_week_growth

    # L2
    multiplier_four_times = 4 # 4 times as much
    third_week_growth = multiplier_four_times * second_week_growth

    # L3
    total_growth = first_week_growth + second_week_growth + third_week_growth

    # FA
    answer = total_growth
    return answer
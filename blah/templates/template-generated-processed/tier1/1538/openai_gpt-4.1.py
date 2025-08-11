def solve():
    """Index: 1538.
    Returns: the total number of paintings Marcus paints in 5 days.
    """
    # L1
    day1_paintings = 2 # 2 paintings on the first day
    multiplier = 2 # twice as many paintings as the day before
    day2_paintings = day1_paintings * multiplier

    # L2
    day3_paintings = day2_paintings * multiplier

    # L3
    day4_paintings = day3_paintings * multiplier

    # L4
    day5_paintings = day4_paintings * multiplier

    # L5
    total_paintings = day1_paintings + day2_paintings + day3_paintings + day4_paintings + day5_paintings

    # FA
    answer = total_paintings
    return answer
def solve():
    """Index: 2671.
    Returns: the amount of rain on the third day.
    """
    # L1
    rain_day1 = 4 # rained 4 inches

    # L2
    multiplier_day2 = 5 # 5 times as much as the first day
    rain_day2 = multiplier_day2 * rain_day1

    # L3
    less_than_sum_day3 = 6 # 6 inches less than the sum of the first two days
    rain_day3 = (rain_day1 + rain_day2) - less_than_sum_day3

    # FA
    answer = rain_day3
    return answer
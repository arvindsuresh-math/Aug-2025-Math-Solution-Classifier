def solve():
    """Index: 2671.
    Returns: the amount of rain in inches on the third day.
    """
    # L1
    first_day_rain = 4 # it rained 4 inches (first day)

    # L2
    second_day_multiplier = 5 # 5 times as much as the first day
    second_day_rain = second_day_multiplier * first_day_rain

    # L3
    third_day_less = 6 # 6 inches less than the sum of the first two days
    third_day_rain = (first_day_rain + second_day_rain) - third_day_less

    # FA
    answer = third_day_rain
    return answer
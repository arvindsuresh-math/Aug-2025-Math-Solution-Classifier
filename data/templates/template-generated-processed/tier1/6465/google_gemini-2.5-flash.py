def solve():
    """Index: 6465.
    Returns: how much less it is raining this year than average.
    """
    # L1
    first_day_rainfall = 26 # On the first day, 26 cm of rain fell
    second_day_rainfall = 34 # On the second day, 34 cm fell
    less_than_second_day = 12 # 12 cm less than the second day fell
    third_day_rainfall = second_day_rainfall - less_than_second_day
    total_rainfall_this_year = first_day_rainfall + second_day_rainfall + third_day_rainfall

    # L2
    average_rainfall_normal_year = 140 # The average rainfall for the first three days of May is usually 140 cm
    less_than_average = average_rainfall_normal_year - total_rainfall_this_year

    # FA
    answer = less_than_average
    return answer
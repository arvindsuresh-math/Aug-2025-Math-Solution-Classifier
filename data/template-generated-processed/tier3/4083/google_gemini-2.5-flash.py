def solve():
    """Index: 4083.
    Returns: the average inches of rain needed per day to finish the year with the normal average.
    """
    # L1
    normal_daily_average_rain = 2 # average of 2 inches of rain a day
    days_in_year = 365 # WK
    total_normal_rain_per_year = days_in_year * normal_daily_average_rain

    # L2
    rain_received_so_far = 430 # they've gotten 430 inches of rain
    rain_needed_more = total_normal_rain_per_year - rain_received_so_far

    # L3
    days_left_in_year = 100 # With 100 days left in the year
    average_rain_needed_per_day = rain_needed_more / days_left_in_year

    # FA
    answer = average_rain_needed_per_day
    return answer
def solve():
    """Index: 4061.
    Returns: the total miles Ken cycled in one week.
    """
    # L1
    twenty_min_intervals_per_hour = 3 # WK
    rain_miles_per_20_min = 30 # 30 miles in 20 minutes
    miles_per_rainy_hour = twenty_min_intervals_per_hour * rain_miles_per_20_min

    # L2
    snow_miles_per_20_min = 10 # 10 miles in 20 minutes
    miles_per_snowy_hour = twenty_min_intervals_per_hour * snow_miles_per_20_min

    # L3
    rain_days = 3 # rains 3 times
    total_miles_rainy_days = miles_per_rainy_hour * rain_days

    # L4
    snow_days = 4 # snows 4 times
    total_miles_snowy_days = miles_per_snowy_hour * snow_days

    # L5
    total_miles_week = total_miles_snowy_days + total_miles_rainy_days

    # FA
    answer = total_miles_week
    return answer
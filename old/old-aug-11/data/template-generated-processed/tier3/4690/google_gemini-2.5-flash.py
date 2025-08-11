def solve():
    """Index: 4690.
    Returns: the total hours Terry spends driving daily.
    """
    # L1
    distance_one_way = 60 # 60 miles away from his home
    trips_per_day = 2 # forth and back
    total_daily_miles = distance_one_way * trips_per_day

    # L2
    speed = 40 # speed of 40 miles per hour
    total_driving_hours = total_daily_miles / speed

    # FA
    answer = total_driving_hours
    return answer
def solve():
    """Index: 6470.
    Returns: the total miles Greg travels.
    """
    # L1
    travel_time_minutes = 30 # travels for 30 minutes
    minutes_per_hour = 60 # WK
    travel_time_hours = travel_time_minutes * (1 / minutes_per_hour)

    # L2
    speed_mph = 20 # 20 miles per hour
    miles_home = travel_time_hours * speed_mph

    # L3
    miles_to_market = 30 # drives 30 miles from his workplace to the farmer's market
    total_miles = miles_home + miles_to_market

    # FA
    answer = total_miles
    return answer
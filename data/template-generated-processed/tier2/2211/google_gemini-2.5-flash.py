def solve():
    """Index: 2211.
    Returns: the car's mileage for a typical week.
    """
    # L1
    school_trip_distance = 2.5 # trip from Philip's house to the children's school is 2.5 miles
    round_trip_school_distance = school_trip_distance + school_trip_distance

    # L2
    school_trips_per_day = 2 # round trip to school two times
    daily_school_mileage = school_trips_per_day * round_trip_school_distance

    # L3
    school_trip_days_per_week = 4 # every day for 4 days a week
    weekly_school_mileage = school_trip_days_per_week * daily_school_mileage

    # L4
    market_trip_distance = 2 # trip to the market is 2 miles
    weekly_market_mileage = market_trip_distance + market_trip_distance

    # L5
    total_weekly_mileage = weekly_school_mileage + weekly_market_mileage

    # FA
    answer = total_weekly_mileage
    return answer
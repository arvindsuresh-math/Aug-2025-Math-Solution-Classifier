def solve():
    """Index: 2211.
    Returns: Philip's car mileage for a typical week.
    """
    # L1
    school_distance_one_way = 2.5 # the trip from Philip's house to the children's school is 2.5 miles
    school_round_trip = school_distance_one_way + school_distance_one_way

    # L2
    school_trips_per_day = 2 # makes the round trip to school two times
    daily_school_mileage = school_trips_per_day * school_round_trip

    # L3
    school_days_per_week = 4 # every day for 4 days a week
    weekly_school_mileage = school_days_per_week * daily_school_mileage

    # L4
    market_distance_one_way = 2 # the trip to the market is 2 miles
    market_round_trip = market_distance_one_way + market_distance_one_way

    # L5
    total_weekly_mileage = weekly_school_mileage + market_round_trip

    # FA
    answer = total_weekly_mileage
    return answer
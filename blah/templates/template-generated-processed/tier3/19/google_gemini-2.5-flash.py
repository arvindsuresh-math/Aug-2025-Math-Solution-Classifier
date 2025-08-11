def solve():
    """Index: 19.
    Returns: the total time Tim spends biking a week.
    """
    # L1
    distance_to_work = 20 # His work is 20 miles away
    round_trip_multiplier = 2 # back and forth
    daily_work_miles = distance_to_work * round_trip_multiplier

    # L2
    workdays_per_week = 5 # 5 workdays
    weekly_work_miles = daily_work_miles * workdays_per_week

    # L3
    weekend_ride_miles = 200 # weekend bike ride of 200 miles
    total_weekly_miles = weekly_work_miles + weekend_ride_miles

    # L4
    biking_speed_mph = 25 # bike at 25 mph
    total_biking_hours = total_weekly_miles / biking_speed_mph

    # FA
    answer = total_biking_hours
    return answer
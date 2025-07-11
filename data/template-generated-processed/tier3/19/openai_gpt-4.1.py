def solve():
    """Index: 19.
    Returns: the total number of hours Tim spends biking in a week.
    """
    # L1
    work_distance_one_way = 20 # his work is 20 miles away
    trips_per_day = 2 # back and forth
    daily_work_miles = work_distance_one_way * trips_per_day

    # L2
    workdays = 5 # 5 workdays
    total_work_miles = daily_work_miles * workdays

    # L3
    weekend_ride_miles = 200 # weekend bike ride of 200 miles
    total_miles = total_work_miles + weekend_ride_miles

    # L4
    bike_speed = 25 # can bike at 25 mph
    total_hours = total_miles / bike_speed

    # FA
    answer = total_hours
    return answer
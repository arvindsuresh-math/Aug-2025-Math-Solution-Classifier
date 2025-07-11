def solve(
        workdays: int = 5, # for each of his 5 workdays
        work_distance_one_way: int = 20, # His work is 20 miles away
        weekend_ride_distance: int = 200, # a weekend bike ride of 200 miles
        bike_speed: int = 25 # bike at 25 mph
    ):
    """Index: 19.
    Returns: the total time Tim spends biking in a week.
    """
    #: L1
    daily_work_distance = work_distance_one_way * 2

    #: L2
    total_work_distance_weekly = daily_work_distance * workdays

    #: L3
    total_weekly_distance = total_work_distance_weekly + weekend_ride_distance

    #: L4
    total_biking_time_hours = total_weekly_distance / bike_speed

    answer = total_biking_time_hours # FINAL ANSWER
    return answer
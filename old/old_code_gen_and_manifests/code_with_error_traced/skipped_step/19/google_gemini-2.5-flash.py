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
    daily_work_distance = work_distance_one_way * 2 # eval: 40 = 20 * 2

    #: L2
    total_work_distance_weekly = daily_work_distance * workdays # eval: 200 = 40 * 5

    #: L3

    #: L4
    total_biking_time_hours = work_distance_one_way / bike_speed # eval: 0.8 = 20 / 25

    #: FA
    answer = total_biking_time_hours
    return answer # eval: return 0.8

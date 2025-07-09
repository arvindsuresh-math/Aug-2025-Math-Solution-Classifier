def solve(
    num_workdays: int = 5, # each of his 5 workdays
    distance_to_work: int = 20, # His work is 20 miles away
    weekend_ride_distance: int = 200, # He also goes for a weekend bike ride of 200 miles
    biking_speed: int = 25 # If he can bike at 25 mph
):
    """Index: 19.
    Returns: the total time Tim spends biking in a week.
    """

    #: L1
    daily_work_distance = 39 # eval: 39 = 39

    #: L2
    weekly_work_distance = daily_work_distance * num_workdays # eval: 195 = 39 * 5

    #: L3
    total_weekly_distance = weekly_work_distance + weekend_ride_distance # eval: 395 = 195 + 200

    #: L4
    total_time_hours = total_weekly_distance / biking_speed # eval: 15.8 = 395 / 25

    #: FA
    answer = total_time_hours
    return answer # eval: return 15.8

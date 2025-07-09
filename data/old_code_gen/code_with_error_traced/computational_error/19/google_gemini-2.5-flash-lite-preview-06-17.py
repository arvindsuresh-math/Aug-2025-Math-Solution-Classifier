def solve(
    work_distance: int = 20, # His work is 20 miles away
    workdays: int = 5, # for each of his 5 workdays
    weekend_ride_distance: int = 200, # He also goes for a weekend bike ride of 200 miles
    biking_speed: int = 25 # If he can bike at 25 mph
):
    """Index: 19.
    Returns: the total time in hours Tim spends biking in a week.
    """

    #: L1
    daily_work_distance = work_distance * 2 # eval: 40 = 20 * 2

    #: L2
    total_work_distance = 190 # eval: 190 = 190

    #: L3
    total_weekly_distance = total_work_distance + weekend_ride_distance # eval: 390 = 190 + 200

    #: L4
    total_time_biking = total_weekly_distance / biking_speed # eval: 15.6 = 390 / 25

    #: FA
    answer = total_time_biking
    return answer # eval: return 15.6

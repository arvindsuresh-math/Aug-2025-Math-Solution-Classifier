def solve(
    workdays: int = 5,  # for each of his 5 workdays
    distance_one_way: int = 20,  # His work is 20 miles away
    weekend_ride: int = 200,  # weekend bike ride of 200 miles
    speed_mph: int = 25  # he can bike at 25 mph
):
    """Index: 19.
    Returns: the total time Tim spends biking in a week in hours.
    """

    #: L1
    daily_work_miles = distance_one_way * 2 # eval: 40 = 20 * 2

    #: L2
    total_work_miles = daily_work_miles * workdays # eval: 200 = 40 * 5

    #: L3
    total_miles = total_work_miles + weekend_ride # eval: 400 = 200 + 200

    #: L4
    total_time_hours = total_miles / speed_mph # eval: 16.0 = 400 / 25

    #: FA
    answer = total_time_hours # eval: 16.0 = 16.0
    return answer # eval: return 16.0

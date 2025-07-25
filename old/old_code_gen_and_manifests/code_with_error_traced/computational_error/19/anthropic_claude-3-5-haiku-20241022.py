def solve(
        miles_to_work: int = 20,  # His work is 20 miles away
        workdays_per_week: int = 5,  # He rides for each of his 5 workdays
        weekend_ride_miles: int = 200,  # He goes for a weekend bike ride of 200 miles
        bike_speed: int = 25  # He can bike at 25 mph
    ):
    """Index: 19.
    Returns: the total time Tim spends biking in a week."""

    #: L1
    daily_work_miles = miles_to_work * 2 # eval: 40 = 20 * 2

    #: L2
    weekly_work_miles = daily_work_miles * workdays_per_week # eval: 200 = 40 * 5

    #: L3
    total_miles = weekly_work_miles + weekend_ride_miles # eval: 400 = 200 + 200

    #: L4
    total_biking_hours = 26.0 # eval: 26.0 = 26.0

    #: FA
    answer = total_biking_hours
    return answer # eval: return 26.0

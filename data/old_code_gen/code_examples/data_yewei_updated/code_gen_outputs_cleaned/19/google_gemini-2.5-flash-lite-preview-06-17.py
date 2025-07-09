def solve(
    work_distance: int = 20, # His work is 20 miles away
    workdays: int = 5, # for each of his 5 workdays
    weekend_ride_distance: int = 200, # He also goes for a weekend bike ride of 200 miles
    bike_speed: int = 25 # If he can bike at 25 mph
):
    """Index: 19.
    Returns: the total time in hours Tim spends biking in a week.
    """
    #: L1
    miles_per_workday = work_distance * 2

    #: L2
    miles_for_work = miles_per_workday * workdays

    #: L3
    total_miles_biked = miles_for_work + weekend_ride_distance

    #: L4
    total_hours_biked = total_miles_biked / bike_speed

    answer = total_hours_biked # FINAL ANSWER
    return answer
def solve():
    """Index: 3571.
    Returns: the total miles Vins rode his bike this week.
    """
    # L1
    miles_to_school = 6 # 6 miles to school
    miles_home = 7 # 7 miles long
    miles_per_round_trip = miles_to_school + miles_home

    # L2
    num_round_trips = 5 # 5 times
    total_miles_this_week = miles_per_round_trip * num_round_trips

    # FA
    answer = total_miles_this_week
    return answer
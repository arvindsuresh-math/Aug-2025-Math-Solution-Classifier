def solve():
    """Index: 5205.
    Returns: the total time the race takes in hours.
    """
    # L1
    total_marathon_miles = 26 # A marathon is 26 miles
    initial_miles_run = 10 # first 10 miles
    remaining_miles = total_marathon_miles - initial_miles_run

    # L2
    initial_pace_mph = 10 # first 10 miles in 1 hour
    pace_reduction_factor = 0.8 # 80% that pace
    reduced_pace_mph = initial_pace_mph * pace_reduction_factor

    # L3
    time_for_remaining_miles = remaining_miles / reduced_pace_mph

    # L4
    initial_time_hours = 1 # 1 hour
    total_race_time = initial_time_hours + time_for_remaining_miles

    # FA
    answer = total_race_time
    return answer
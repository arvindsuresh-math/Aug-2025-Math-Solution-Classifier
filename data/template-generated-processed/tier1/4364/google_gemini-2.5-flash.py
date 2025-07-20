def solve():
    """Index: 4364.
    Returns: the number of miles Jackson is running each day at the end of this exercise program.
    """
    # L1
    num_weeks = 4 # next four weeks
    extra_mile_per_week = 1 # one additional mile/day each week
    additional_miles = num_weeks * extra_mile_per_week

    # L2
    initial_miles_per_day = 3 # running 3 miles a day the first week
    final_miles_per_day = additional_miles + initial_miles_per_day

    # FA
    answer = final_miles_per_day
    return answer
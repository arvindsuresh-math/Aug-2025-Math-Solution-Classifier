def solve():
    """Index: 3905.
    Returns: the total number of laps Jasmine swims in five weeks.
    """
    # L2
    laps_per_day = 12 # swims 12 laps every afternoon
    days_per_week = 5 # Monday through Friday
    laps_per_week = laps_per_day * days_per_week

    # L3
    num_weeks = 5 # in five weeks
    total_laps = num_weeks * laps_per_week

    # FA
    answer = total_laps
    return answer
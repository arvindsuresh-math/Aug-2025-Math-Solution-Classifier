def solve():
    """Index: 6893.
    Returns: how many minutes faster Samuel finished his homework than Sarah.
    """
    # L1
    minutes_per_hour = 60 # WK
    sarah_time_hours = 1.3 # Sarah took 1.3 hours
    sarah_time_minutes = sarah_time_hours * minutes_per_hour

    # L2
    samuel_time_minutes = 30 # Samuel took 30 minutes
    time_difference_minutes = sarah_time_minutes - samuel_time_minutes

    # FA
    answer = time_difference_minutes
    return answer
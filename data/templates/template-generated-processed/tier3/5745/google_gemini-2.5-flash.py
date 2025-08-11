def solve():
    """Index: 5745.
    Returns: the number of turns Barry can take standing on his head.
    """
    # L1
    headstand_duration = 10 # stands on his head for 10 minutes
    rest_duration = 5 # sit for 5 minutes
    total_turn_duration = headstand_duration + rest_duration

    # L2
    hours_period = 2 # single 2-hour period
    minutes_per_hour = 60 # WK
    total_minutes_period = minutes_per_hour * hours_period

    # L3
    number_of_turns = total_minutes_period / total_turn_duration

    # FA
    answer = number_of_turns
    return answer
def solve():
    """Index: 5323.
    Returns: the time it takes Tom to climb the hill in hours.
    """
    # L1
    elizabeth_time_minutes = 30 # Elizabeth takes 30 minutes
    tom_multiplier = 4 # Tom takes four times as long
    tom_time_minutes = elizabeth_time_minutes * tom_multiplier

    # L2
    minutes_per_hour = 60 # WK
    tom_time_hours = tom_time_minutes / minutes_per_hour

    # FA
    answer = tom_time_hours
    return answer
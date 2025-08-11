def solve():
    """Index: 7156.
    Returns: the average time in minutes it took Rich to run a mile.
    """
    # L1
    hours_run = 3 # 3 hours
    minutes_per_hour = 60 # WK
    hours_to_minutes = hours_run * minutes_per_hour

    # L2
    additional_minutes = 36 # 36 minutes
    total_minutes = hours_to_minutes + additional_minutes

    # L3
    total_miles = 24 # 24-mile marathon
    minutes_per_mile = total_minutes / total_miles

    # FA
    answer = minutes_per_mile
    return answer
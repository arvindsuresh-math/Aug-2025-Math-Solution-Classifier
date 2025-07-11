def solve():
    """Index: 2879.
    Returns: the total number of hours Malcolm spends brushing his teeth.
    """
    # L1
    times_per_day = 3 # 3 times a day
    minutes_per_brushing = 2 # 2 minutes
    minutes_per_day = times_per_day * minutes_per_brushing

    # L2
    number_of_days = 30 # After 30 days
    total_minutes_brushed = minutes_per_day * number_of_days

    # L3
    minutes_per_hour = 60 # 60 minutes in 1 hour
    total_hours_brushed = total_minutes_brushed / minutes_per_hour

    # FA
    answer = total_hours_brushed
    return answer
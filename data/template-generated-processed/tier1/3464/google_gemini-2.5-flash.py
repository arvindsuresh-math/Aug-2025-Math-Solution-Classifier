def solve():
    """Index: 3464.
    Returns: the total meters Lisa walks in two days.
    """
    # L1
    minutes_per_hour = 60 # WK
    hours_walked_per_day = 1 # walks for an hour
    minutes_walked_per_day = hours_walked_per_day * minutes_per_hour

    # L2
    meters_per_minute = 10 # 10 meters each minute
    meters_walked_per_day = minutes_walked_per_day * meters_per_minute

    # L3
    num_days = 2 # two days
    total_meters_walked = meters_walked_per_day * num_days

    # FA
    answer = total_meters_walked
    return answer
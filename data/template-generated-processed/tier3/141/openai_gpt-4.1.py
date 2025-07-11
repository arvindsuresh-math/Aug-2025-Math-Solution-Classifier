def solve():
    """Index: 141.
    Returns: the total number of minutes Larry spends on his dog each day.
    """
    # L1
    minutes_per_half_hour = 30 # half an hour
    walks_per_day = 2 # twice a day
    walking_minutes = minutes_per_half_hour * walks_per_day

    # L2
    minutes_per_hour = 60 # WK
    feeding_divisor = 5 # a fifth of an hour
    feeding_minutes = minutes_per_hour / feeding_divisor

    # L3
    total_minutes = walking_minutes + feeding_minutes

    # FA
    answer = total_minutes
    return answer
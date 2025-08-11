def solve():
    """Index: 3178.
    Returns: the total meters Isabel runs during a week.
    """
    # L1
    circuit_length = 365 # circuit that is 365 meters long
    morning_runs = 7 # 7 times in the morning
    morning_distance = morning_runs * circuit_length

    # L2
    afternoon_runs = 3 # 3 times in the afternoon
    afternoon_distance = afternoon_runs * circuit_length

    # L3
    daily_distance = morning_distance + afternoon_distance

    # L4
    days_in_week = 7 # WK
    weekly_distance = days_in_week * daily_distance

    # FA
    answer = weekly_distance
    return answer
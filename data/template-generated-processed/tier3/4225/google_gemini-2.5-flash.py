def solve():
    """Index: 4225.
    Returns: the average number of seconds per minute Jason shoots flames.
    """
    # L1
    fire_interval_seconds = 15 # every 15 seconds
    seconds_per_minute = 60 # WK
    times_fired_per_minute = seconds_per_minute / fire_interval_seconds

    # L2
    flame_duration_seconds = 5 # shoot a flame for 5 seconds
    total_flame_seconds_per_minute = times_fired_per_minute * flame_duration_seconds

    # FA
    answer = total_flame_seconds_per_minute
    return answer
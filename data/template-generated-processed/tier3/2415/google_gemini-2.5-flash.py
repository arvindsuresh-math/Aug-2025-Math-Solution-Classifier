def solve():
    """Index: 2415.
    Returns: the number of snowflakes at first.
    """
    # L1
    minutes_per_hour = 60 # WK
    interval_minutes = 5 # every 5 minutes
    num_intervals = minutes_per_hour / interval_minutes

    # L2
    snowflakes_per_interval = 4 # an additional 4 snowflakes
    snowflakes_fell = num_intervals * snowflakes_per_interval

    # L3
    total_snowflakes_after_hour = 58 # 58 snowflakes after 1 hour
    initial_snowflakes = total_snowflakes_after_hour - snowflakes_fell

    # FA
    answer = initial_snowflakes
    return answer
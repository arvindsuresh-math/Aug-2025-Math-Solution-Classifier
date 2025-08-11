def solve():
    """Index: 2301.
    Returns: the total number of minutes passed.
    """
    # L1
    total_snowflakes_target = 58 # 58 snowflakes
    initial_snowflakes = 10 # 10 snowflakes at first
    snowflakes_needed = total_snowflakes_target - initial_snowflakes

    # L2
    snowflakes_per_interval = 4 # an additional 4 snowflakes every 5 minutes
    num_intervals = snowflakes_needed / snowflakes_per_interval

    # L3
    minutes_per_interval = 5 # every 5 minutes
    total_minutes_passed = num_intervals * minutes_per_interval

    # FA
    answer = total_minutes_passed
    return answer
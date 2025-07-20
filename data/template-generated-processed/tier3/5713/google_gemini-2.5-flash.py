def solve():
    """Index: 5713.
    Returns: the total mile time for all three people.
    """
    # L1
    tina_time = 6 # Tina, who with a time of 6 minutes
    tony_speed_factor = 2 # twice as fast as Tina
    tony_time = tina_time / tony_speed_factor

    # L2
    tom_speed_factor = 3 # one-third as fast a runner as Tom (implies Tom is 3 times faster than Tina)
    tom_time = tina_time / tom_speed_factor

    # L3
    total_time = tina_time + tony_time + tom_time

    # FA
    answer = total_time
    return answer
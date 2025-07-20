def solve():
    """Index: 4781.
    Returns: the difference in miles Joseph drives compared to Kyle.
    """
    # L1
    joseph_speed = 50 # Joseph drives his car at 50 mph
    joseph_time = 2.5 # for 2.5 hours
    joseph_distance = joseph_speed * joseph_time

    # L2
    kyle_speed = 62 # Kyle drives his car at 62 mph
    kyle_time = 2 # for 2 hours
    kyle_distance = kyle_speed * kyle_time

    # L3
    difference_in_distance = joseph_distance - kyle_distance

    # FA
    answer = difference_in_distance
    return answer
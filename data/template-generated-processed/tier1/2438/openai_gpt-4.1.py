def solve():
    """Index: 2438.
    Returns: the number of tennis balls Brian has.
    """
    # L1
    lily_balls = 3 # Lily has 3 tennis balls
    frodo_more_than_lily = 8 # Frodo has 8 more than Lily
    frodo_balls = frodo_more_than_lily + lily_balls

    # L2
    brian_times_frodo = 2 # Brian has twice as many as Frodo
    brian_balls = frodo_balls * brian_times_frodo

    # FA
    answer = brian_balls
    return answer
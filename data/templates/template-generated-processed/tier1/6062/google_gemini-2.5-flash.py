def solve():
    """Index: 6062.
    Returns: the total number of bowling balls.
    """
    # L1
    red_balls = 30 # 30 red bowling balls
    more_green_than_red = 6 # 6 more green bowling balls than red
    green_balls = red_balls + more_green_than_red

    # L2
    total_balls = red_balls + green_balls

    # FA
    answer = total_balls
    return answer
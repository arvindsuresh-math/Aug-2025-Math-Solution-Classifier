def solve():
    """Index: 7001.
    Returns: the number of balloons Andrew has left.
    """
    # L1
    blue_balloons = 303 # 303 blue balloons
    purple_balloons = 453 # 453 purple balloons
    total_balloons = blue_balloons + purple_balloons

    # L2
    share_divisor = 2 # shares half of his balloons
    balloons_left = total_balloons / share_divisor

    # FA
    answer = balloons_left
    return answer
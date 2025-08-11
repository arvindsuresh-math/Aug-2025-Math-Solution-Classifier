def solve():
    """Index: 3398.
    Returns: the percentage of yellow balls carried.
    """
    # L1
    yellow_balls = 27 # 27 yellow balls
    brown_balls = 33 # 33 brown balls
    total_balls = yellow_balls + brown_balls

    # L2
    percentage_multiplier = 100 # 100%
    percentage_yellow_balls = (yellow_balls / total_balls) * percentage_multiplier

    # FA
    answer = percentage_yellow_balls
    return answer
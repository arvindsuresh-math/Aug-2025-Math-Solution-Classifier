def solve():
    """Index: 6337.
    Returns: the total number of balloons.
    """
    # L1
    gold_balloons = 141 # 141 gold balloons

    # L2
    multiplier_silver = 2 # twice as many silver balloons
    silver_balloons = gold_balloons * multiplier_silver

    # L3
    black_balloons = 150 # 150 black balloons
    total_balloons = gold_balloons + silver_balloons + black_balloons

    # FA
    answer = total_balloons
    return answer
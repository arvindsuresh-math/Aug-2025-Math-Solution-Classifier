def solve():
    """Index: 1729.
    Returns: the total number of insects Calvin has in his collection.
    """
    # L1
    roaches = 12 # 12 giant roaches
    cricket_divisor = 2 # half as many crickets as roaches
    crickets = roaches / cricket_divisor

    # L2
    scorpions = 3 # 3 scorpions
    caterpillar_multiplier = 2 # twice as many caterpillars as scorpions
    caterpillars = scorpions * caterpillar_multiplier

    # L3
    total_insects = roaches + scorpions + crickets + caterpillars

    # FA
    answer = total_insects
    return answer
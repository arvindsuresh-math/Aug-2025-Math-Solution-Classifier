def solve():
    """Index: 5106.
    Returns: the difference in height between Grace's tower and Clyde's tower.
    """
    # L1
    grace_tower_height = 40 # Grace’s tower is 8 times the size of Clyde’s at 40 inches tall
    clyde_tower_ratio_denominator = 8 # 8 times the size of Clyde’s
    clyde_tower_height = grace_tower_height / clyde_tower_ratio_denominator

    # L2
    height_difference = grace_tower_height - clyde_tower_height

    # FA
    answer = height_difference
    return answer
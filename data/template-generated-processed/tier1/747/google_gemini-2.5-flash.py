def solve():
    """Index: 747.
    Returns: the combined height of the two rockets.
    """
    # L1
    rocket1_height = 500 # 500 ft in the air
    multiplier_twice = 2 # twice as high
    rocket2_height = rocket1_height * multiplier_twice

    # L2
    combined_height = rocket1_height + rocket2_height

    # FA
    answer = combined_height
    return answer
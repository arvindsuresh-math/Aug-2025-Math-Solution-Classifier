def solve():
    """Index: 7225.
    Returns: the total billions of miles traveled by the Zargon Destroyer.
    """
    # L1
    normal_space_hours = 7 # seven hours in normal space
    normal_space_speed = 2 # 2 billion miles per hour in normal space
    normal_space_distance = normal_space_hours * normal_space_speed

    # L2
    black_hole_speed_multiplier = 3 # three times faster
    black_hole_speed = black_hole_speed_multiplier * normal_space_speed

    # L3
    black_hole_hours = 2 # two hours through a black hole
    black_hole_distance = black_hole_hours * black_hole_speed

    # L4
    total_distance = normal_space_distance + black_hole_distance

    # FA
    answer = total_distance
    return answer
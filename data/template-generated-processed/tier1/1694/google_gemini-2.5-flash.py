def solve():
    """Index: 1694.
    Returns: the total distance Carson walks in one night.
    """
    # L1
    warehouse_length = 600 # 600 feet long
    num_long_sides = 2 # WK
    distance_long_sides = warehouse_length * num_long_sides

    # L2
    warehouse_width = 400 # 400 feet wide
    num_short_sides = 2 # WK
    distance_short_sides = warehouse_width * num_short_sides

    # L3
    distance_one_circle = distance_long_sides + distance_short_sides

    # L4
    planned_circles = 10 # circle the warehouse 10 times
    skipped_circles = 2 # skips 2 times
    actual_circles = planned_circles - skipped_circles

    # L5
    total_distance_walked = distance_one_circle * actual_circles

    # FA
    answer = total_distance_walked
    return answer
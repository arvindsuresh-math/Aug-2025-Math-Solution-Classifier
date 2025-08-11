def solve():
    """Index: 1694.
    Returns: the total distance Carson walks in one night.
    """
    # L1
    long_side = 600 # 600 feet long
    num_long_sides = 2 # 2 sides
    long_sides_distance = long_side * num_long_sides

    # L2
    short_side = 400 # 400 feet wide
    num_short_sides = 2 # 2 sides
    short_sides_distance = short_side * num_short_sides

    # L3
    distance_per_circle = long_sides_distance + short_sides_distance

    # L4
    supposed_circles = 10 # circle the warehouse 10 times
    skipped_circles = 2 # skips 2 times
    actual_circles = supposed_circles - skipped_circles

    # L5
    total_distance = distance_per_circle * actual_circles

    # FA
    answer = total_distance
    return answer
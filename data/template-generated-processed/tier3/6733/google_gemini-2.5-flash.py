def solve():
    """Index: 6733.
    Returns: the total cost of paint.
    """
    # L1
    flag_width = 5 # 5 feet wide
    flag_height = 4 # 4 feet tall
    area_per_side = flag_width * flag_height

    # L2
    num_sides = 2 # paint both sides
    total_paintable_area = num_sides * area_per_side

    # L3
    coverage_per_quart = 4 # a quart is good for 4 square feet
    quarts_needed = total_paintable_area / coverage_per_quart

    # L4
    cost_per_quart = 2 # Paint costs $2 a quart
    total_cost = quarts_needed * cost_per_quart

    # FA
    answer = total_cost
    return answer
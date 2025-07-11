def solve():
    """Index: 1833.
    Returns: the number of gallon cans of paint Linda needs to buy.
    """
    # L1
    num_coats = 2 # two coats
    wall_area_per_coat = 600 # The wall area is 600 sq. ft.
    total_area_to_paint = num_coats * wall_area_per_coat

    # L2
    coverage_per_gallon = 400 # a gallon of paint can cover 400 sq. ft.
    cans_needed = total_area_to_paint / coverage_per_gallon

    # FA
    answer = cans_needed
    return answer
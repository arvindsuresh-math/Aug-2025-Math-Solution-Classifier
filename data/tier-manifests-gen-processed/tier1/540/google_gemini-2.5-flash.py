def solve():
    """Index: 540.
    Returns: the total number of sides on the cookie cutters.
    """
    # L1
    num_triangles = 6 # 6 cookie cutters shaped like triangles
    sides_per_triangle = 3 # WK
    total_sides_triangles = num_triangles * sides_per_triangle

    # L2
    num_squares = 4 # 4 square ones
    sides_per_square = 4 # WK
    total_sides_squares = num_squares * sides_per_square

    # L3
    num_hexagons = 2 # 2 hexagons
    sides_per_hexagon = 6 # WK
    total_sides_hexagons = num_hexagons * sides_per_hexagon

    # L4
    total_sides = total_sides_triangles + total_sides_squares + total_sides_hexagons

    # FA
    answer = total_sides
    return answer
def solve():
    """Index: 540.
    Returns: the total number of sides on all the cookie cutters.
    """
    # L1
    num_triangles = 6 # 6 cookie cutters shaped like triangles
    sides_per_triangle = 3 # triangles have 3 sides each
    triangle_sides = num_triangles * sides_per_triangle

    # L2
    num_squares = 4 # 4 square ones
    sides_per_square = 4 # squares have 4 sides each
    square_sides = num_squares * sides_per_square

    # L3
    num_hexagons = 2 # 2 hexagons
    sides_per_hexagon = 6 # hexagons have 6 sides each
    hexagon_sides = num_hexagons * sides_per_hexagon

    # L4
    total_sides = triangle_sides + square_sides + hexagon_sides

    # FA
    answer = total_sides
    return answer
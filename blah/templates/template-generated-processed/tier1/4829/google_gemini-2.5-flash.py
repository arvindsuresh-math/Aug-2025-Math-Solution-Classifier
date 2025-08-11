def solve():
    """Index: 4829.
    Returns: the total number of lines Bill drew.
    """
    # L1
    num_triangles = 12 # 12 triangles
    sides_per_triangle = 3 # WK
    lines_from_triangles = num_triangles * sides_per_triangle

    # L2
    num_squares = 8 # 8 squares
    sides_per_square = 4 # WK
    lines_from_squares = num_squares * sides_per_square

    # L3
    num_pentagons = 4 # 4 pentagons
    sides_per_pentagon = 5 # WK
    lines_from_pentagons = num_pentagons * sides_per_pentagon

    # L4
    total_lines = lines_from_triangles + lines_from_squares + lines_from_pentagons

    # FA
    answer = total_lines
    return answer
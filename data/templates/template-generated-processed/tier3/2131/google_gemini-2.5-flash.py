def solve():
    """Index: 2131.
    Returns: the number of right triangles that fit inside the square.
    """
    # L1
    triangle_height = 2 # height of 2 inches
    triangle_width = 2 # width of two inches
    triangle_area_factor = 0.5 # WK
    triangle_area = triangle_area_factor * triangle_height * triangle_width

    # L2
    square_side = 2 # square with 2-inch sides
    square_area = square_side * square_side

    # L3
    num_triangles_fit = square_area / triangle_area

    # FA
    answer = num_triangles_fit
    return answer
def solve():
    """Index: 1588.
    Returns: the total square inches of canvas needed.
    """
    # L1
    rectangular_sail_length = 5 # a rectangular sail that measures 5 inches
    rectangular_sail_width = 8 # by 8 inches
    rectangular_sail_area = rectangular_sail_length * rectangular_sail_width

    # L2
    first_triangle_base_square = 3 # one that's 3 inches long at the bottom
    first_triangle_height_square = 4 # and 4 inches tall
    first_triangle_equivalent_square_area = first_triangle_base_square * first_triangle_height_square

    # L3
    triangle_divisor = 2 # dividing the area of a square with the same height and length by 2
    first_triangular_sail_area = first_triangle_equivalent_square_area / triangle_divisor

    # L4
    second_triangle_base_square = 4 # one that's 4 inches long at the bottom
    second_triangle_height_square = 6 # and 6 inches tall
    second_triangle_equivalent_square_area = second_triangle_base_square * second_triangle_height_square

    # L5
    second_triangular_sail_area = second_triangle_equivalent_square_area / triangle_divisor

    # L6
    total_canvas_needed = second_triangular_sail_area + first_triangular_sail_area + rectangular_sail_area

    # FA
    answer = total_canvas_needed
    return answer
def solve():
    """Index: 6716.
    Returns: the percentage of ink left in the marker.
    """
    # L1
    square_side_length = 4 # 4 inch by 4 inch squares
    square_area = square_side_length * square_side_length

    # L2
    num_squares = 3 # three 4 inch by 4 inch squares
    total_ink_capacity = num_squares * square_area

    # L3
    rectangle_width = 6 # 6 inch by 2 inch rectangles
    rectangle_height = 2 # 6 inch by 2 inch rectangles
    rectangle_area = rectangle_width * rectangle_height

    # L4
    num_rectangles = 2 # two 6 inch by 2 inch rectangles
    total_ink_used = num_rectangles * rectangle_area

    # L5
    fraction_ink_left = total_ink_used / total_ink_capacity

    # L6
    percentage_multiplier = 100 # WK
    percentage_ink_left = fraction_ink_left * percentage_multiplier

    # FA
    answer = percentage_ink_left
    return answer
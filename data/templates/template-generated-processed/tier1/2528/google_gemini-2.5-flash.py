def solve():
    """Index: 2528.
    Returns: the difference in area between the two shapes.
    """
    # L1
    rectangle_length = 3 # length of 3 inches
    rectangle_width = 6 # width of 6 inches
    rectangle_area = rectangle_length * rectangle_width

    # L2
    square_width = 5 # width of 5 inches
    square_area = square_width * square_width

    # L3
    difference_in_area = square_area - rectangle_area

    # FA
    answer = difference_in_area
    return answer
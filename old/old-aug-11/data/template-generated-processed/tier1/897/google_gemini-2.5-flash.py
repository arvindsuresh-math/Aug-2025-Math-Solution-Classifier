def solve():
    """Index: 897.
    Returns: the height of the computer screen in cm.
    """
    # L1
    sides_in_square = 4 # WK
    side_length_square = 20 # side of the square paper is 20 cm
    perimeter_square = sides_in_square * side_length_square

    # L2
    shorter_amount = 20 # 20 cm shorter than the height
    height_screen = shorter_amount + perimeter_square

    # FA
    answer = height_screen
    return answer
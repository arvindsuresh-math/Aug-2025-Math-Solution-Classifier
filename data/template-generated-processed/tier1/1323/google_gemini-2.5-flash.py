def solve():
    """Index: 1323.
    Returns: the length of each side of the square quilt.
    """
    # L1
    quilt_length = 6 # 6 feet
    quilt_width = 24 # 24 feet
    quilt_area = quilt_length * quilt_width

    # L2
    side_length_square = int(quilt_area**0.5)

    # FA
    answer = side_length_square
    return answer
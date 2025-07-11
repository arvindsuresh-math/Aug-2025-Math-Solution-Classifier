def solve():
    """Index: 897.
    Returns: the height of the computer screen in cm.
    """
    # L1
    num_sides = 4 # WK
    side_length = 20 # side of the square is 20 cm
    perimeter = num_sides * side_length

    # L2
    shorter_by = 20 # perimeter is 20 cm shorter than the height
    height = shorter_by + perimeter

    # FA
    answer = height
    return answer
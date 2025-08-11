def solve():
    """Index: 793.
    Returns: the area of the rectangle.
    """
    # L1
    perimeter = 30 # perimeter is 30 inches
    width = 4 # 4 inches wide
    sides_multiplier = 2 # WK
    twice_height = perimeter - sides_multiplier * width

    # L2
    height_divisor = 2 # WK
    height = twice_height / height_divisor

    # L3
    area = width * height

    # FA
    answer = area
    return answer
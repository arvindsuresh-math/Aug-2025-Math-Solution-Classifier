def solve():
    """Index: 2640.
    Returns: the number of rectangles required to reach the target length.
    """
    # L1
    area = 1638 # an area of 1638
    width = 42 # a width of 42 inches
    rectangle_length = area / width

    # L2
    target_length = 390 # reach a length of 390 inches
    num_rectangles = target_length / rectangle_length

    # FA
    answer = num_rectangles
    return answer
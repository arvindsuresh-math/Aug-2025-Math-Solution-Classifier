def solve():
    """Index: 1598.
    Returns: the sum of the height and width of the Great Pyramid of Giza in feet.
    """
    # L1
    base_height = 500 # 500 feet
    taller_by = 20 # 20 feet taller than 500 feet
    height = base_height + taller_by

    # L2
    wider_by = 234 # 234 feet wider than it is tall
    width = height + wider_by

    # L3
    sum_height_width = height + width

    # FA
    answer = sum_height_width
    return answer
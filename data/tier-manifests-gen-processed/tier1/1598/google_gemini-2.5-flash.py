def solve():
    """Index: 1598.
    Returns: the sum of the height and width of the Great Pyramid of Giza in feet.
    """
    # L1
    base_height = 500 # 500 feet
    taller_than_base = 20 # 20 feet taller
    height = base_height + taller_than_base

    # L2
    wider_than_tall = 234 # 234 feet wider than it is tall
    width = height + wider_than_tall

    # L3
    sum_height_width = height + width

    # FA
    answer = sum_height_width
    return answer
def solve():
    """Index: 7152.
    Returns: the total number of pieces of sea glass Dorothy had.
    """
    # L1
    blanche_red_glass = 3 # 3 pieces of red sea glass
    rose_red_glass = 9 # 9 pieces of red
    total_red_blanche_rose = blanche_red_glass + rose_red_glass

    # L2
    multiplier_dorothy_red = 2 # twice as many pieces of red glass
    dorothy_red_glass = multiplier_dorothy_red * total_red_blanche_rose

    # L3
    rose_blue_glass = 11 # 11 pieces of blue sea glass
    multiplier_dorothy_blue = 3 # three times as much blue sea glass as Rose
    dorothy_blue_glass = rose_blue_glass * multiplier_dorothy_blue

    # L4
    dorothy_total_glass = dorothy_red_glass + dorothy_blue_glass

    # FA
    answer = dorothy_total_glass
    return answer
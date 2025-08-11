def solve():
    """Index: 2592.
    Returns: the total liters of fruit punch they had for the picnic.
    """
    # L1
    orange_punch = 4.5 # 4.5 liters of orange punch

    # L2
    cherry_multiplier = 2 # twice as much cherry punch as orange punch
    cherry_punch = cherry_multiplier * orange_punch

    # L3
    apple_less_than_cherry = 1.5 # 1.5 liters less of apple juice than cherry punch
    apple_punch = cherry_punch - apple_less_than_cherry

    # L4
    total_punch = orange_punch + cherry_punch + apple_punch

    # FA
    answer = total_punch
    return answer
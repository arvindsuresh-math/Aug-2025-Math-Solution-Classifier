def solve():
    """Index: 2592.
    Returns: the total liters of fruit punch.
    """
    # L1
    orange_punch_liters = 4.5 # 4.5 liters of orange punch

    # L2
    cherry_multiplier = 2 # twice as much cherry punch
    cherry_punch_liters = cherry_multiplier * orange_punch_liters

    # L3
    apple_less_cherry = 1.5 # 1.5 liters less of apple juice
    apple_juice_liters = cherry_punch_liters - apple_less_cherry

    # L4
    total_punch_liters = orange_punch_liters + cherry_punch_liters + apple_juice_liters

    # FA
    answer = total_punch_liters
    return answer
def solve():
    """Index: 505.
    Returns: the number of sheep out in the wilderness.
    """
    # L1
    sheep_in_pen = 81 # 81 sheep in the pen
    rounded_up_percent_decimal = 0.9 # 90% rounded up
    total_sheep = sheep_in_pen / rounded_up_percent_decimal

    # L2
    wandered_percent_num = 10 # 10% wandered off
    percent_factor = 0.01 # WK
    sheep_in_hills = total_sheep * wandered_percent_num * percent_factor

    # FA
    answer = sheep_in_hills
    return answer
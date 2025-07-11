def solve():
    """Index: 505.
    Returns: the number of sheep out in the wilderness.
    """
    # L1
    sheep_in_pen = 81 # 81 sheep in the pen
    rounded_up_decimal = 0.9 # 90% of her sheep
    total_sheep = sheep_in_pen / rounded_up_decimal

    # L2
    wandered_off_percent = 10 # remaining 10% wandered off
    percent_to_decimal_factor = 0.01 # WK
    sheep_in_wilderness = total_sheep * wandered_off_percent * percent_to_decimal_factor

    # FA
    answer = sheep_in_wilderness
    return answer
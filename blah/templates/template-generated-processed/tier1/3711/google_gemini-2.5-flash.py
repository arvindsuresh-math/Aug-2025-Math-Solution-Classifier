def solve():
    """Index: 3711.
    Returns: the number of bananas Katherine has.
    """
    # L1
    num_apples = 4 # 4 apples
    multiplier_pears = 3 # 3 times as many pears
    num_pears = multiplier_pears * num_apples

    # L2
    total_apples_pears = num_apples + num_pears

    # L3
    total_fruit = 21 # total of 21 pieces of fruit
    num_bananas = total_fruit - total_apples_pears

    # FA
    answer = num_bananas
    return answer
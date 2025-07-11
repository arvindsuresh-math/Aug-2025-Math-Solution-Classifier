def solve():
    """Index: 430.
    Returns: the number of plums Tanya bought.
    """
    # L1
    remaining_fruit = 9 # 9 pieces remaining
    half_multiplier = 2 # WK
    total_fruit_bought = half_multiplier * remaining_fruit

    # L2
    pears = 6 # 6 pears
    granny_smith_apples = 4 # 4 Granny Smith apples
    pineapples = 2 # 2 pineapples
    plums = total_fruit_bought - pears - granny_smith_apples - pineapples

    # FA
    answer = plums
    return answer
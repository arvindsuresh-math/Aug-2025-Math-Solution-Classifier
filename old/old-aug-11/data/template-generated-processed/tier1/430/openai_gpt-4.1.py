def solve():
    """Index: 430.
    Returns: the number of plums Tanya bought.
    """
    # L1
    fruit_left = 9 # there were only 9 pieces remaining
    total_fruit = 2 * fruit_left

    # L2
    pears = 6 # 6 pears
    apples = 4 # 4 Granny Smith apples
    pineapples = 2 # 2 pineapples
    plums = total_fruit - pears - apples - pineapples

    # FA
    answer = plums
    return answer
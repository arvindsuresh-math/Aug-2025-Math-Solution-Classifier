def solve():
    """Index: 4311.
    Returns: the total number of fruits on the display.
    """
    # L1
    bananas = 5 # 5 bananas on the display
    orange_multiplier = 2 # twice as many oranges
    oranges = bananas * orange_multiplier

    # L2
    apple_multiplier = 2 # twice as many apples
    apples = oranges * apple_multiplier

    # L3
    total_fruits = apples + oranges + bananas

    # FA
    answer = total_fruits
    return answer
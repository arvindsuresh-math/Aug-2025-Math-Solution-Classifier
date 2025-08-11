def solve():
    """Index: 5929.
    Returns: the number of oranges in the bowl.
    """
    # L1
    num_bananas = 2 # 2 bananas
    apple_multiplier = 2 # twice as many apples
    num_apples = num_bananas * apple_multiplier

    # L2
    total_fruits = 12 # 12 fruits in the bowl
    num_oranges = total_fruits - num_apples - num_bananas

    # FA
    answer = num_oranges
    return answer
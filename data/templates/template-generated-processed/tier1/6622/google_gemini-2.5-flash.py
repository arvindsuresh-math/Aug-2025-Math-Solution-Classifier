def solve():
    """Index: 6622.
    Returns: the total number of fruits Marley has.
    """
    # L1
    louis_oranges = 5 # Louis has 5 oranges
    multiplier_oranges = 2 # twice as many oranges
    marley_oranges = multiplier_oranges * louis_oranges

    # L2
    samantha_apples = 7 # Samantha has 7 apples
    multiplier_apples = 3 # three times as many apples
    marley_apples = multiplier_apples * samantha_apples

    # L3
    total_marley_fruits = marley_oranges + marley_apples

    # FA
    answer = total_marley_fruits
    return answer
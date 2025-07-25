def solve():
    """Index: 6769.
    Returns: the total number of fish Ken and Kendra brought home.
    """
    # L1
    kendra_caught = 30 # Kendra caught 30 fish
    ken_multiplier = 2 # twice as many fish as Kendra
    ken_caught = kendra_caught * ken_multiplier

    # L2
    ken_released = 3 # Ken released 3 fish
    ken_brought_home = ken_caught - ken_released

    # L3
    total_brought_home = ken_brought_home + kendra_caught

    # FA
    answer = total_brought_home
    return answer
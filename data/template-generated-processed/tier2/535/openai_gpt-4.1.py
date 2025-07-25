def solve():
    """Index: 535.
    Returns: the total amount Tim paid for eggs.
    """
    # L1
    dozens_bought = 3 # Tim buys 3 dozen eggs
    eggs_per_dozen = 12 # WK
    total_eggs = dozens_bought * eggs_per_dozen

    # L2
    cost_per_egg = 0.5 # Eggs cost $.50 each
    total_cost = total_eggs * cost_per_egg

    # FA
    answer = total_cost
    return answer
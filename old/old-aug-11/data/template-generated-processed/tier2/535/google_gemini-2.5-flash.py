def solve():
    """Index: 535.
    Returns: the total cost Tim paid for eggs.
    """
    # L1
    num_dozens = 3 # 3 dozen eggs
    eggs_per_dozen = 12 # WK
    total_eggs = num_dozens * eggs_per_dozen

    # L2
    cost_per_egg = 0.50 # $.50 each
    total_cost = total_eggs * cost_per_egg

    # FA
    answer = total_cost
    return answer
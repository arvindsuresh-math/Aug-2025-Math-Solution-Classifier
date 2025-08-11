def solve():
    """Index: 5078.
    Returns: the difference between the eggs that are still in perfect condition and those that are cracked.
    """
    # L1
    num_dozen_eggs = 2 # 2 dozen eggs
    dozen = 12 # WK
    total_initial_eggs = num_dozen_eggs * dozen

    # L2
    broken_eggs = 3 # 3 eggs broke
    cracked_multiplier = 2 # twice as many cracked
    cracked_eggs = broken_eggs * cracked_multiplier

    # L3
    perfect_eggs = total_initial_eggs - broken_eggs - cracked_eggs

    # L4
    difference_perfect_cracked = perfect_eggs - cracked_eggs

    # FA
    answer = difference_perfect_cracked
    return answer
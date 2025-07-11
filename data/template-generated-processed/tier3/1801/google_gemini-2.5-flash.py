def solve():
    """Index: 1801.
    Returns: the number of eggs left on the shelf.
    """
    # L1
    num_dozens_bought = 6 # six dozen eggs
    eggs_per_dozen = 12 # WK
    total_eggs_bought = num_dozens_bought * eggs_per_dozen

    # L2
    half_divisor = 2 # used half of the eggs
    eggs_after_use = total_eggs_bought / half_divisor

    # L3
    broken_eggs = 15 # broke 15 of the remaining eggs
    eggs_left = eggs_after_use - broken_eggs

    # FA
    answer = eggs_left
    return answer
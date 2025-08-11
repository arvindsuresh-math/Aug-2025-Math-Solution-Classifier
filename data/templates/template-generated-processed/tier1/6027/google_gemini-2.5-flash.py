def solve():
    """Index: 6027.
    Returns: the total number of eggs the family has now.
    """
    # L1
    initial_eggs = 10 # 10 eggs
    eggs_used_for_omelet = 5 # used 5 of them
    eggs_after_omelet = initial_eggs - eggs_used_for_omelet

    # L2
    num_chickens = 2 # 2 chickens
    eggs_per_chicken = 3 # laid 3 eggs each
    new_eggs_laid = num_chickens * eggs_per_chicken

    # L3
    total_eggs = eggs_after_omelet + new_eggs_laid

    # FA
    answer = total_eggs
    return answer
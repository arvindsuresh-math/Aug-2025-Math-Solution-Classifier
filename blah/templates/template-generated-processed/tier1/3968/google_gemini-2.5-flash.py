def solve():
    """Index: 3968.
    Returns: the number of eggs Linda broke.
    """
    # L1
    total_eggs_left = 12 # a dozen eggs left
    brown_eggs_survived = 5 # all 5 of the brown eggs survived
    white_eggs_left = total_eggs_left - brown_eggs_survived

    # L2
    white_eggs_multiplier = 3 # three times as many white eggs as brown eggs
    original_white_eggs = white_eggs_multiplier * brown_eggs_survived

    # L3
    broken_white_eggs = original_white_eggs - white_eggs_left

    # FA
    answer = broken_white_eggs
    return answer
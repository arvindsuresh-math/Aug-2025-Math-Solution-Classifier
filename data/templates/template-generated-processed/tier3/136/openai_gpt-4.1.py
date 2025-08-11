def solve():
    """Index: 136.
    Returns: the total number of sticks of wax Loraine used for all the animals.
    """
    # L1
    sticks_small_animal = 2 # small animals take two sticks
    sticks_small_total = 12 # she used 12 sticks of wax for small animals
    num_small_animals = sticks_small_total / sticks_small_animal

    # L2
    small_to_large_ratio = 3 # three times as many small animals as large animals
    num_large_animals = num_small_animals / small_to_large_ratio

    # L3
    sticks_large_animal = 4 # large animals take four sticks
    sticks_large_total = num_large_animals * sticks_large_animal

    # L4
    total_sticks = sticks_small_total + sticks_large_total

    # FA
    answer = total_sticks
    return answer
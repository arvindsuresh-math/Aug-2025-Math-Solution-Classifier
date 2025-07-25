def solve():
    """Index: 136.
    Returns: the total number of sticks of wax used for all animals.
    """
    # L1
    sticks_for_small_animals = 12 # used 12 sticks of wax for small animals
    sticks_per_small_animal = 2 # small animals take two sticks
    num_small_animals = sticks_for_small_animals / sticks_per_small_animal

    # L2
    small_to_large_ratio = 3 # three times as many small animals as large animals
    num_large_animals = num_small_animals / small_to_large_ratio

    # L3
    sticks_per_large_animal = 4 # Large animals take four sticks of wax
    sticks_for_large_animals = num_large_animals * sticks_per_large_animal

    # L4
    total_sticks_used = sticks_for_small_animals + sticks_for_large_animals

    # FA
    answer = total_sticks_used
    return answer
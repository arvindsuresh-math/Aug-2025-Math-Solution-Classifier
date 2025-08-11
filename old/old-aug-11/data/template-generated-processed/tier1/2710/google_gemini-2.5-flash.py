def solve():
    """Index: 2710.
    Returns: the total number of animals on the farm.
    """
    # L1
    current_cows = 2 # 2 cows
    current_pigs = 3 # 3 pigs
    current_goats = 6 # 6 goats
    current_total_animals = current_cows + current_pigs + current_goats

    # L2
    added_cows = 3 # adding 3 cows
    added_pigs = 5 # adding 5 pigs
    added_goats = 2 # adding 2 goats
    added_total_animals = added_cows + added_pigs + added_goats

    # L3
    final_total_animals = current_total_animals + added_total_animals

    # FA
    answer = final_total_animals
    return answer
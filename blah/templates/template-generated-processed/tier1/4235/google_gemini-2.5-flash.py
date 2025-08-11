def solve():
    """Index: 4235.
    Returns: the original population of the town before new people moved in.
    """
    # L1
    final_population = 60 # After 4 years, the population is 60 people
    halving_factor = 2 # WK
    population_end_year_3 = final_population * halving_factor

    # L2
    population_end_year_2 = population_end_year_3 * halving_factor

    # L3
    population_end_year_1 = population_end_year_2 * halving_factor

    # L4
    original_moved_out = 400 # 400 of the original population move out
    population_before_original_move_out = population_end_year_1 + original_moved_out

    # L5
    new_people_moved_in = 100 # 100 new people move into a town
    original_population = population_before_original_move_out - new_people_moved_in

    # FA
    answer = original_population
    return answer
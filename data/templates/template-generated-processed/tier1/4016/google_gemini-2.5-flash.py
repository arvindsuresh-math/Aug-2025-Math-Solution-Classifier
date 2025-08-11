def solve():
    """Index: 4016.
    Returns: the real number of animals in the petting zoo.
    """
    # L1
    mary_total_animals = 60 # Mary thinks there are 60 animals
    double_counted_sheep = 7 # double-counts 7 sheep
    animals_after_subtracting_double_count = mary_total_animals - double_counted_sheep

    # L2
    forgotten_pigs = 3 # forgets to count 3 pigs
    real_total_animals = animals_after_subtracting_double_count + forgotten_pigs

    # FA
    answer = real_total_animals
    return answer
def solve():
    """Index: 3360.
    Returns: the total time it would take to see all animal types.
    """
    # L1
    initial_species = 5 # 5 different types of animals
    new_species_imported = 4 # import 4 new species
    total_species = initial_species + new_species_imported

    # L2
    time_per_animal_type = 6 # around 6 minutes
    total_time_minutes = total_species * time_per_animal_type

    # FA
    answer = total_time_minutes
    return answer
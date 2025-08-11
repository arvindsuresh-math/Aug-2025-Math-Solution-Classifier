def solve():
    """Index: 531.
    Returns: the total number of hours the zoo spent recovering animals.
    """
    # L1
    num_lions = 3 # 3 lions
    num_rhinos = 2 # 2 rhinos
    total_animals = num_lions + num_rhinos

    # L2
    hours_per_animal = 2 # 2 hours to recover each animal
    total_hours = total_animals * hours_per_animal

    # FA
    answer = total_hours
    return answer
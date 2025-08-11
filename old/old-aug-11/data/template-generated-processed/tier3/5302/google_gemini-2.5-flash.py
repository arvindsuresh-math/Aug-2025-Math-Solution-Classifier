def solve():
    """Index: 5302.
    Returns: the number of omelets each person gets.
    """
    # L1
    num_dozens = 3 # three dozen eggs
    eggs_per_dozen = 12 # WK
    total_eggs = num_dozens * eggs_per_dozen

    # L2
    eggs_per_omelet = 4 # Each omelet requires 4 eggs
    total_omelets = total_eggs / eggs_per_omelet

    # L3
    num_people = 3 # there are 3 people
    omelets_per_person = total_omelets / num_people

    # FA
    answer = omelets_per_person
    return answer
def solve():
    """Index: 3204.
    Returns: the number of eggs each person gets.
    """
    # L1
    num_dozens = 2 # two dozen eggs
    eggs_per_dozen = 12 # WK
    total_eggs = num_dozens * eggs_per_dozen

    # L2
    mark_count = 1 # Mark has
    num_siblings = 3 # his three siblings
    total_eaters = mark_count + num_siblings

    # L3
    eggs_per_person = total_eggs / total_eaters

    # FA
    answer = eggs_per_person
    return answer
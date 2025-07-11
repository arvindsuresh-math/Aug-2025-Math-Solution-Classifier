def solve():
    """Index: 1085.
    Returns: the total number of suitcases the entire family is bringing on vacation.
    """
    # L1
    num_siblings = 4 # 4 siblings
    suitcases_per_sibling = 2 # 2 suitcases
    siblings_total_suitcases = num_siblings * suitcases_per_sibling

    # L2
    num_parents = 2 # WK
    suitcases_per_parent = 3 # 3 suitcases
    parents_total_suitcases = num_parents * suitcases_per_parent

    # L3
    total_suitcases = siblings_total_suitcases + parents_total_suitcases

    # FA
    answer = total_suitcases
    return answer
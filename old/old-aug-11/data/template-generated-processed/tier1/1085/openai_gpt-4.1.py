def solve():
    """Index: 1085.
    Returns: the total number of suitcases the family is bringing on vacation.
    """
    # L1
    num_siblings = 4 # 4 siblings
    suitcases_per_sibling = 2 # 2 suitcases each
    sibling_suitcases = num_siblings * suitcases_per_sibling

    # L2
    num_parents = 2 # parents (implied: mother and father)
    suitcases_per_parent = 3 # 3 suitcases each
    parent_suitcases = num_parents * suitcases_per_parent

    # L3
    total_suitcases = sibling_suitcases + parent_suitcases

    # FA
    answer = total_suitcases
    return answer
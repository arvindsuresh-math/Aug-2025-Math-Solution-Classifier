def solve():
    """Index: 878.
    Returns: the total number of fruits Santino has.
    """
    # L1
    num_papaya_trees = 2 # 2 papaya trees
    papayas_per_tree = 10 # each papaya tree produces 10 papayas
    total_papayas = num_papaya_trees * papayas_per_tree

    # L2
    num_mango_trees = 3 # 3 mango trees
    mangos_per_tree = 20 # each mango tree produces 20 mangos
    total_mangos = num_mango_trees * mangos_per_tree

    # L3
    total_fruits = total_papayas + total_mangos

    # FA
    answer = total_fruits
    return answer
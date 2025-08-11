def solve():
    """Index: 878.
    Returns: the total number of fruits Santino has.
    """
    # L1
    num_papaya_trees = 2 # 2 papaya trees
    papayas_per_tree = 10 # 10 papayas
    total_papaya_fruits = num_papaya_trees * papayas_per_tree

    # L2
    num_mango_trees = 3 # 3 mango trees
    mangos_per_tree = 20 # 20 mangos
    total_mango_fruits = num_mango_trees * mangos_per_tree

    # L3
    total_fruits = total_papaya_fruits + total_mango_fruits

    # FA
    answer = total_fruits
    return answer
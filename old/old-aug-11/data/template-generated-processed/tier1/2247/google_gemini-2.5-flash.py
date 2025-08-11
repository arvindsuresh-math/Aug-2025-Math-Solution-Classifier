def solve():
    """Index: 2247.
    Returns: the age difference between the first and second tree in years.
    """
    # L1
    fat_rings_per_group = 2 # two fat rings
    thin_rings_per_group = 4 # four thin rings
    total_rings_per_group = fat_rings_per_group + thin_rings_per_group

    # L2
    groups_tree1 = 70 # 70 ring groups in the first tree
    groups_tree2 = 40 # 40 ring groups in the second tree
    difference_in_groups = groups_tree1 - groups_tree2

    # L3
    age_difference_in_rings = difference_in_groups * total_rings_per_group

    # FA
    answer = age_difference_in_rings
    return answer
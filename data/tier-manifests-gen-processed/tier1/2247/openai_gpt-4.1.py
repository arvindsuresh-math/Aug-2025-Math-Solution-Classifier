def solve():
    """Index: 2247.
    Returns: how much older the first tree is than the second tree, in years.
    """
    # L1
    fat_rings_per_group = 2 # two fat rings
    thin_rings_per_group = 4 # four thin rings
    rings_per_group = fat_rings_per_group + thin_rings_per_group

    # L2
    groups_first_tree = 70 # 70 ring groups in the first tree
    groups_second_tree = 40 # 40 ring groups in the second tree
    group_difference = groups_first_tree - groups_second_tree

    # L3
    age_difference = group_difference * rings_per_group

    # FA
    answer = age_difference
    return answer
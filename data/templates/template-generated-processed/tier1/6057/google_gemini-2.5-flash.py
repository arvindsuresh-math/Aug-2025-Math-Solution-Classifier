def solve():
    """Index: 6057.
    Returns: the total number of leaves on all the trees.
    """
    # L1
    num_branches = 10 # 10 branches
    sub_branches_per_branch = 40 # 40 sub-branches
    total_sub_branches_per_tree = num_branches * sub_branches_per_branch

    # L2
    leaves_per_sub_branch = 60 # 60 leaves each
    leaves_per_tree = leaves_per_sub_branch * total_sub_branches_per_tree

    # L3
    total_trees_on_farm = 4 # total number of trees on the farm is 4
    total_leaves_on_all_trees = leaves_per_tree * total_trees_on_farm

    # FA
    answer = total_leaves_on_all_trees
    return answer
def solve():
    """Index: 3245.
    Returns: the total number of leaves on the tree.
    """
    # L1
    num_branches = 30 # 30 branches
    twigs_per_branch = 90 # 90 twigs per branch
    total_twigs = num_branches * twigs_per_branch

    # L2
    percent_four_leaves = 30 # 30% of the twigs
    percent_to_decimal_factor = 0.01 # WK
    twigs_four_leaves = total_twigs * percent_four_leaves * percent_to_decimal_factor

    # L3
    twigs_five_leaves = total_twigs - twigs_four_leaves

    # L4
    leaves_per_twig_five = 5 # rest sprout 5 leaves
    total_leaves_five = twigs_five_leaves * leaves_per_twig_five

    # L5
    leaves_per_twig_four = 4 # sprout 4 leaves
    total_leaves_four = twigs_four_leaves * leaves_per_twig_four

    # L6
    total_leaves_on_tree = total_leaves_five + total_leaves_four

    # FA
    answer = total_leaves_on_tree
    return answer
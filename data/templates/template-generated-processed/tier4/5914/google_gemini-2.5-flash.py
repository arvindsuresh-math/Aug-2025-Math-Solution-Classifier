def solve():
    """Index: 5914.
    Returns: the total number of trees Salaria has.
    """
    # L1
    tree_a_total_oranges = 10 # Tree A gives her 10 oranges a month
    tree_a_good_percent = 0.6 # 60% are good
    good_oranges_tree_a = tree_a_total_oranges * tree_a_good_percent

    # L2
    tree_b_total_oranges = 15 # Tree B gives her 15 oranges
    tree_b_good_fraction_numerator = 1 # 1/3 are good
    tree_b_good_fraction_denominator = 3 # 1/3 are good
    good_oranges_tree_b = tree_b_total_oranges * (tree_b_good_fraction_numerator / tree_b_good_fraction_denominator)

    # L3
    tree_a_proportion = 0.5 # 50% of tree A
    tree_b_proportion = 0.5 # 50% of tree B
    average_good_oranges_per_tree = tree_a_proportion * good_oranges_tree_a + tree_b_proportion * good_oranges_tree_b

    # L4
    total_good_oranges_per_month = 55 # 55 good oranges per month
    total_trees = total_good_oranges_per_month / average_good_oranges_per_tree

    # FA
    answer = total_trees
    return answer
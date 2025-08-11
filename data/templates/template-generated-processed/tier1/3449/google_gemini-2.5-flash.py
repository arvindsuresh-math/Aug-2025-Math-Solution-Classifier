def solve():
    """Index: 3449.
    Returns: the total number of apples that can be gotten from 10 trees.
    """
    # L1
    baskets_per_tree = 20 # An apple tree can fill 20 baskets
    apples_per_basket = 15 # Each basket can be filled with 15 apples
    apples_per_tree = baskets_per_tree * apples_per_basket

    # L2
    num_trees = 10 # from 10 trees
    total_apples = apples_per_tree * num_trees

    # FA
    answer = total_apples
    return answer
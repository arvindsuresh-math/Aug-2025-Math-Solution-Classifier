def solve():
    """Index: 263.
    Returns: the total money John makes from selling apples.
    """
    # L1
    trees_row = 3 # 3 trees
    trees_column = 4 # 4 trees
    total_trees = trees_row * trees_column

    # L2
    apples_per_tree = 5 # Each tree gives 5 apples
    total_apples = total_trees * apples_per_tree

    # L3
    price_per_apple = 0.5 # sells each apple for $.5
    total_money = total_apples * price_per_apple

    # FA
    answer = total_money
    return answer
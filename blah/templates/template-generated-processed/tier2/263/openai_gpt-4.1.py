def solve():
    """Index: 263.
    Returns: the total money John makes from selling all the apples, in dollars.
    """
    # L1
    num_rows = 3 # 3 trees
    num_columns = 4 # 4 trees
    num_trees = num_rows * num_columns

    # L2
    apples_per_tree = 5 # Each tree gives 5 apples
    total_apples = num_trees * apples_per_tree

    # L3
    price_per_apple = 0.5 # sells each apple for $.5
    total_money = total_apples * price_per_apple

    # FA
    answer = total_money
    return answer
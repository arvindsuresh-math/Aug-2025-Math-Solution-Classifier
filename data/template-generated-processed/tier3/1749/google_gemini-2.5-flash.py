def solve():
    """Index: 1749.
    Returns: the total profit John made.
    """
    # L1
    num_trees = 30 # John chops down 30 trees
    planks_per_tree = 25 # From each tree, he can make 25 planks
    total_planks = num_trees * planks_per_tree

    # L2
    planks_per_table = 15 # A table takes 15 planks to make
    num_tables = total_planks / planks_per_table

    # L3
    table_price = 300 # sells for $300
    total_revenue = num_tables * table_price

    # L4
    labor_cost = 3000 # He paid $3000 for all the labor
    profit = total_revenue - labor_cost

    # FA
    answer = profit
    return answer
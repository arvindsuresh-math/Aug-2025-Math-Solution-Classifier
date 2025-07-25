def solve():
    """Index: 1815.
    Returns: the total number of trees Jim has after doubling them.
    """
    # L1
    initial_rows = 2 # 2 rows of 4 trees
    trees_per_row = 4 # 4 trees
    initial_trees = initial_rows * trees_per_row

    # L2
    final_age = 15 # 15th birthday
    start_planting_age = 10 # turns 10
    years_planting = final_age - start_planting_age

    # L3
    trees_planted_total = years_planting * trees_per_row

    # L4
    trees_before_doubling = trees_planted_total + initial_trees

    # L5
    doubling_factor = 2 # doubles the number of trees
    final_trees = trees_before_doubling * doubling_factor

    # FA
    answer = final_trees
    return answer
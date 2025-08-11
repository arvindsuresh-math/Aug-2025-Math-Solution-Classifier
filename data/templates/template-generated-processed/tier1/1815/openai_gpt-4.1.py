def solve():
    """Index: 1815.
    Returns: the number of trees Jim has after doubling them on his 15th birthday.
    """
    # L1
    initial_rows = 2 # 2 rows of 4 trees
    trees_per_row = 4 # 4 trees per row
    initial_trees = initial_rows * trees_per_row

    # L2
    birthday_final = 15 # 15th birthday
    birthday_start = 10 # starts planting at 10
    years_planting = birthday_final - birthday_start

    # L3
    trees_planted = years_planting * trees_per_row

    # L4
    total_before_doubling = trees_planted + initial_trees

    # L5
    total_after_doubling = total_before_doubling * 2

    # FA
    answer = total_after_doubling
    return answer
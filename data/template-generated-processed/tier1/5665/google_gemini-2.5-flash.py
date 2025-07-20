def solve():
    """Index: 5665.
    Returns: the total number of homes in Mariam's neighborhood.
    """
    # L1
    houses_one_side = 40 # 40 houses on one side of the main road
    multiplier = 3 # three times as many homes
    houses_other_side = multiplier * houses_one_side

    # L2
    total_homes = houses_one_side + houses_other_side

    # FA
    answer = total_homes
    return answer
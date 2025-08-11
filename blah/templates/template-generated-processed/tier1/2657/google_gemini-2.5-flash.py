def solve():
    """Index: 2657.
    Returns: the number of doughnuts left.
    """
    # L1
    num_dozens = 2 # 2 dozen doughnuts
    dozen = 12 # WK
    total_doughnuts_initial = num_dozens * dozen

    # L2
    eaten_doughnuts = 8 # ate 8 doughnuts
    doughnuts_left = total_doughnuts_initial - eaten_doughnuts

    # FA
    answer = doughnuts_left
    return answer
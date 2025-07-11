def solve():
    """Index: 2657.
    Returns: the number of doughnuts left after the family ate 8.
    """
    # L1
    num_dozen = 2 # 2 dozen doughnuts
    dozen = 12 # WK
    total_doughnuts = num_dozen * dozen

    # L2
    doughnuts_eaten = 8 # family ate 8 doughnuts
    doughnuts_left = total_doughnuts - doughnuts_eaten

    # FA
    answer = doughnuts_left
    return answer
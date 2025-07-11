def solve():
    """Index: 3946.
    Returns: the number of brownies on the counter at the end.
    """
    # L1
    num_dozen_initial = 2 # 2 dozen brownies
    dozen = 12 # WK
    initial_brownies = num_dozen_initial * dozen

    # L2
    father_ate = 8 # ate 8 of them
    after_father = initial_brownies - father_ate

    # L3
    mooney_ate = 4 # ate 4 of the brownies
    after_mooney = after_father - mooney_ate

    # L4
    num_dozen_second_batch = 2 # another two dozen brownies
    second_batch = num_dozen_second_batch * dozen

    # L5
    total_brownies = after_mooney + second_batch

    # FA
    answer = total_brownies
    return answer
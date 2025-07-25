def solve():
    """Index: 4857.
    Returns: the number of pigeons left.
    """
    # L1
    num_pigeons = 40 # 40 pigeons
    chicks_per_pigeon = 6 # 6 chicks
    total_chicks = num_pigeons * chicks_per_pigeon

    # L2
    total_pigeons = total_chicks + num_pigeons

    # L3
    percent_eaten_num = 30 # 30%
    percent_factor = 0.01 # WK
    pigeons_eaten = total_pigeons * percent_eaten_num * percent_factor

    # L4
    pigeons_left = total_pigeons - pigeons_eaten

    # FA
    answer = pigeons_left
    return answer
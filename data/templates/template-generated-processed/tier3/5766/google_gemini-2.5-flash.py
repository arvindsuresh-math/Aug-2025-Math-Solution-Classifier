def solve():
    """Index: 5766.
    Returns: the total number of guppies the four friends have altogether.
    """
    # L1
    haylee_dozens = 3 # 3 dozen guppies
    dozen = 12 # WK
    haylee_guppies = haylee_dozens * dozen

    # L2
    jose_divisor = 2 # half as many guppies
    jose_guppies = haylee_guppies / jose_divisor

    # L3
    charliz_divisor = 3 # one-third of what Jose has
    charliz_guppies = jose_guppies / charliz_divisor

    # L4
    nicolai_multiplier = 4 # 4 times as many guppies
    nicolai_guppies = charliz_guppies * nicolai_multiplier

    # L5
    total_guppies = haylee_guppies + jose_guppies + charliz_guppies + nicolai_guppies

    # FA
    answer = total_guppies
    return answer
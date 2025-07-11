from fractions import Fraction

def solve():
    """Index: 319.
    Returns: the number of diaries Natalie's sister has now.
    """
    # L1
    initial_diaries = 8 # 8 small diaries in her locker
    double_multiplier = 2 # double the number of diaries
    bought_diaries = double_multiplier * initial_diaries

    # L2
    total_after_buying = bought_diaries + initial_diaries

    # L3
    lost_fraction = Fraction(1, 4) # lost 1/4 of what she had
    lost_diaries = lost_fraction * total_after_buying

    # L4
    diaries_now = total_after_buying - lost_diaries

    # FA
    answer = diaries_now
    return answer
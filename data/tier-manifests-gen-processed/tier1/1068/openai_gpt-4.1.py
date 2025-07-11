def solve():
    """Index: 1068.
    Returns: the total number of points Matt scored in the first quarter.
    """
    # L1
    points_per_2pt = 2 # 2-point shots
    num_2pt = 4 # four times
    score_2pt = points_per_2pt * num_2pt

    # L2
    points_per_3pt = 3 # 3-point shots
    num_3pt = 2 # twice
    score_3pt = points_per_3pt * num_3pt

    # L3
    total_score = score_2pt + score_3pt

    # FA
    answer = total_score
    return answer
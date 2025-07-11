def solve():
    """Index: 1068.
    Returns: the total points Matt scored for the quarter.
    """
    # L1
    points_per_2pt_shot = 2 # 2-point shots
    num_2pt_shots = 4 # four times
    total_2pt_score = points_per_2pt_shot * num_2pt_shots

    # L2
    points_per_3pt_shot = 3 # 3-point shots
    num_3pt_shots = 2 # twice
    total_3pt_score = points_per_3pt_shot * num_3pt_shots

    # L3
    total_quarter_score = total_2pt_score + total_3pt_score

    # FA
    answer = total_quarter_score
    return answer
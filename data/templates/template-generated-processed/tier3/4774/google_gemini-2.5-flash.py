def solve():
    """Index: 4774.
    Returns: the average jump of the winner.
    """
    # L1
    athlete1_long_jump = 26 # 26 feet in the long jump
    athlete1_triple_jump = 30 # 30 feet in the triple jump
    athlete1_high_jump = 7 # 7 feet in the high jump
    athlete1_total_jump = athlete1_long_jump + athlete1_triple_jump + athlete1_high_jump

    # L2
    athlete2_long_jump = 24 # 24 feet in the long jump
    athlete2_triple_jump = 34 # 34 feet in the triple jump
    athlete2_high_jump = 8 # 8 feet in the high jump
    athlete2_total_jump = athlete2_long_jump + athlete2_triple_jump + athlete2_high_jump

    # L3
    number_of_jumps = 3 # WK
    athlete1_average_jump = athlete1_total_jump / number_of_jumps

    # L4
    athlete2_average_jump = athlete2_total_jump / number_of_jumps

    # L5
    winner_average_jump = max(athlete1_average_jump, athlete2_average_jump)

    # FA
    answer = winner_average_jump
    return answer
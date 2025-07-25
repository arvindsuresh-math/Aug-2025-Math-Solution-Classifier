def solve():
    """Index: 7258.
    Returns: the total points Tim scored.
    """
    # L1
    single_line_points = 1000 # A single line is worth 1000 points
    tetris_multiplier = 8 # A tetris is worth 8 times that much
    tetris_points = tetris_multiplier * single_line_points

    # L2
    num_tetrises = 4 # 4 tetrises
    total_tetris_points = num_tetrises * tetris_points

    # L3
    num_singles = 6 # 6 singles
    total_single_points = num_singles * single_line_points

    # L4
    total_score = total_tetris_points + total_single_points

    # FA
    answer = total_score
    return answer
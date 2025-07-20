def solve():
    """Index: 3422.
    Returns: the total time in minutes to finish both puzzles.
    """
    # L1
    minutes_per_100_pieces = 10 # 10 minutes
    pieces_in_10_minutes = 100 # 100 pieces
    minutes_per_piece = minutes_per_100_pieces / pieces_in_10_minutes

    # L2
    pieces_per_puzzle = 2000 # 2000 pieces each
    minutes_for_one_puzzle = pieces_per_puzzle * minutes_per_piece

    # L3
    num_puzzles = 2 # 2 puzzles
    total_time_minutes = minutes_for_one_puzzle * num_puzzles

    # FA
    answer = total_time_minutes
    return answer
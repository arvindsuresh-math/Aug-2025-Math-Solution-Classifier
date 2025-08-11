def solve():
    """Index: 7155.
    Returns: the total number of days to complete all puzzles.
    """
    # L1
    num_puzzles_type1 = 8 # eight puzzles
    pieces_per_puzzle_type1 = 300 # 300 pieces each
    total_pieces_type1 = num_puzzles_type1 * pieces_per_puzzle_type1

    # L2
    num_puzzles_type2 = 5 # five puzzles
    pieces_per_puzzle_type2 = 500 # 500 pieces each
    total_pieces_type2 = num_puzzles_type2 * pieces_per_puzzle_type2

    # L3
    total_all_pieces = total_pieces_type1 + total_pieces_type2

    # L4
    max_hours_per_day = 7 # maximum of 7 hours each day
    pieces_per_hour = 100 # 100 pieces per hour
    pieces_per_day = max_hours_per_day * pieces_per_hour

    # L5
    total_days = total_all_pieces / pieces_per_day

    # FA
    answer = total_days
    return answer
def solve():
    """Index: 1258.
    Returns: the total time in minutes to find every Waldo.
    """
    # L1
    num_books = 15 # 15 "Where's Waldo?" books published
    puzzles_per_book = 30 # 30 puzzles to find Waldo
    total_puzzles = num_books * puzzles_per_book

    # L2
    time_per_puzzle = 3 # 3 minutes to find Waldo in a puzzle
    total_time_minutes = total_puzzles * time_per_puzzle

    # FA
    answer = total_time_minutes
    return answer
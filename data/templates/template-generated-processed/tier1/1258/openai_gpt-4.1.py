def solve():
    """Index: 1258.
    Returns: the total time in minutes to find every Waldo in all books.
    """
    # L1
    num_books = 15 # 15 "Where's Waldo?" books published
    puzzles_per_book = 30 # Each book has 30 puzzles
    total_puzzles = num_books * puzzles_per_book

    # L2
    minutes_per_puzzle = 3 # average person takes 3 minutes to find Waldo in a puzzle
    total_minutes = total_puzzles * minutes_per_puzzle

    # FA
    answer = total_minutes
    return answer
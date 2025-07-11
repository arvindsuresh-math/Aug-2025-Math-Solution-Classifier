def solve():
    """Index: 297.
    Returns: the average number of words in each crossword puzzle.
    """
    # L1
    weeks_per_pencil = 2 # every two weeks
    days_per_week = 7 # 7 days a week
    days_per_pencil = weeks_per_pencil * days_per_week

    # L2
    words_per_pencil = 1050 # it takes him 1050 words to use up a pencil
    words_per_puzzle = words_per_pencil / days_per_pencil

    # FA
    answer = words_per_puzzle
    return answer
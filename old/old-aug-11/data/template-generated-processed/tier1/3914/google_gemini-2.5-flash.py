def solve():
    """Index: 3914.
    Returns: the total time Tony spent solving puzzles.
    """
    # L1
    warm_up_time = 10 # took 10 minutes
    multiplier = 3 # 3 times as long
    long_puzzle_time = multiplier * warm_up_time

    # L2
    num_long_puzzles = 2 # 2 puzzles
    total_long_puzzles_time = long_puzzle_time * num_long_puzzles

    # L3
    total_time_spent = total_long_puzzles_time + warm_up_time

    # FA
    answer = total_time_spent
    return answer
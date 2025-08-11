def solve():
    """Index: 7018.
    Returns: the number of matchsticks left in the box.
    """
    # L1
    elvis_num_squares = 5 # Elvis makes 5 squares
    elvis_matchsticks_per_square = 4 # 4-matchstick squares
    elvis_total_matchsticks = elvis_num_squares * elvis_matchsticks_per_square

    # L2
    ralph_num_squares = 3 # Ralph makes 3
    ralph_matchsticks_per_square = 8 # 8-matchstick squares
    ralph_total_matchsticks = ralph_matchsticks_per_square * ralph_num_squares

    # L3
    total_used_matchsticks = elvis_total_matchsticks + ralph_total_matchsticks

    # L4
    initial_matchsticks = 50 # box containing 50 matchsticks
    matchsticks_left = initial_matchsticks - total_used_matchsticks

    # FA
    answer = matchsticks_left
    return answer
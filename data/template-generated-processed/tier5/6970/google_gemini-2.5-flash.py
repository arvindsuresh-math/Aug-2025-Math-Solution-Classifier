def solve():
    """Index: 6970.
    Returns: the number of donated toys that were Joel's.
    """
    # L3
    stuffed_animals = 18 # 18 stuffed animals
    action_figures = 42 # 42 action figures
    board_games = 2 # 2 board games
    puzzles = 13 # 13 puzzles
    friends_donated_toys = stuffed_animals + action_figures + board_games + puzzles

    # L5
    total_donated_toys = 108 # In all, Joel was able to donate 108 toys
    sister_and_joel_combined_toys = total_donated_toys - friends_donated_toys

    # L6
    sister_and_joel_ratio_sum = 3 # derived from T + 2T = 3T
    sister_donated_toys = sister_and_joel_combined_toys / sister_and_joel_ratio_sum

    # L7
    joel_multiplier = 2 # twice as many toys
    joel_donated_toys = joel_multiplier * sister_donated_toys

    # FA
    answer = joel_donated_toys
    return answer
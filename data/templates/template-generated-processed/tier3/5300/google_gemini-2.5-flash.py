def solve():
    """Index: 5300.
    Returns: the average hits per game Javier needs in the remaining games.
    """
    # L1
    initial_games = 20 # first 20 games
    games_left = 10 # 10 games left
    total_games_in_season = initial_games + games_left

    # L2
    target_average_hits = 3 # 3 hits a game
    total_hits_needed = total_games_in_season * target_average_hits

    # L3
    average_hits_first_games = 2 # averaged 2 hits
    hits_already_achieved = initial_games * average_hits_first_games

    # L4
    hits_needed_in_remaining_games = total_hits_needed - hits_already_achieved

    # L5
    average_hits_needed_per_game = hits_needed_in_remaining_games / games_left

    # FA
    answer = average_hits_needed_per_game
    return answer
def solve():
    """Index: 975.
    Returns: the total number of free throws John makes.
    """
    # L1
    total_games = 20 # 20 games the team plays
    games_played_percent = 0.8 # 80% of the 20 games
    games_played = total_games * games_played_percent

    # L2
    fouls_per_game = 5 # gets fouled 5 times a game
    total_fouls = games_played * fouls_per_game

    # L3
    shots_per_foul = 2 # gets 2 shots
    total_foul_shots = total_fouls * shots_per_foul

    # L4
    free_throw_percentage = 0.7 # hits 70% of his free throws
    free_throws_made = total_foul_shots * free_throw_percentage

    # FA
    answer = free_throws_made
    return answer
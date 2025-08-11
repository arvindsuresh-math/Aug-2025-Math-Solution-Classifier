def solve():
    """Index: 975.
    Returns: the number of free throws John makes if he plays in 80% of the 20 games.
    """
    # L1
    total_games = 20 # 20 games the team plays
    percent_played = 0.8 # plays in 80% of the games
    games_played = total_games * percent_played

    # L2
    fouls_per_game = 5 # gets fouled 5 times a game
    total_fouls = games_played * fouls_per_game

    # L3
    shots_per_foul = 2 # for every foul he gets 2 shots
    total_shots = total_fouls * shots_per_foul

    # L4
    hit_percent = 0.7 # hits 70% of his free throws
    made_shots = total_shots * hit_percent

    # FA
    answer = made_shots
    return answer
def solve():
    """Index: 1553.
    Returns: the number of players on the team who did not play that day.
    """
    # L1
    players_start_first_half = 11 # 11 players start the game
    substitutions_first_half = 2 # 2 substitutions made
    players_played_first_half = players_start_first_half + substitutions_first_half

    # L2
    multiplier_second_half_subs = 2 # twice as many substitutions
    substitutions_second_half = multiplier_second_half_subs * substitutions_first_half

    # L3
    total_players_played = players_played_first_half + substitutions_second_half

    # L4
    total_players_prepared = 24 # 24 players prepared for a soccer game
    players_did_not_play = total_players_prepared - total_players_played

    # FA
    answer = players_did_not_play
    return answer
def solve():
    """Index: 1553.
    Returns: the number of players on the team who did not play that day.
    """
    # L1
    starters = 11 # 11 players start the game
    first_half_subs = 2 # 2 substitutions made in the first half
    first_half_players = starters + first_half_subs

    # L2
    second_half_subs = first_half_subs * 2 # twice as many substitutions as in the first half

    # L3
    total_players_played = first_half_players + second_half_subs

    # L4
    total_team = 24 # 24 players prepared for a soccer game
    did_not_play = total_team - total_players_played

    # FA
    answer = did_not_play
    return answer
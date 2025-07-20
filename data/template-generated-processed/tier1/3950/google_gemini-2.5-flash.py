def solve():
    """Index: 3950.
    Returns: the total number of matches played by both teams.
    """
    # L1
    home_team_wins = 3 # home team has won three matches
    multiplier_rival_wins = 2 # won twice as many matches
    rival_team_wins = multiplier_rival_wins * home_team_wins

    # L2
    matches_drawn_per_team = 4 # each team drew four matches
    num_teams = 2 # both teams
    total_drawn_matches = num_teams * matches_drawn_per_team

    # L3
    total_matches_played = home_team_wins + rival_team_wins + total_drawn_matches

    # FA
    answer = total_matches_played
    return answer
def solve():
    """Index: 1734.
    Returns: the total points the team will have after 5 games.
    """
    # L1
    num_games = 5 # after 5 games
    wade_avg_points = 20 # Wade's average points per game is 20
    wade_total_points = num_games * wade_avg_points

    # L2
    teammates_avg_points = 40 # teammates' average points per game is 40
    teammates_total_points = teammates_avg_points * num_games

    # L3
    total_team_points = wade_total_points + teammates_total_points

    # FA
    answer = total_team_points
    return answer
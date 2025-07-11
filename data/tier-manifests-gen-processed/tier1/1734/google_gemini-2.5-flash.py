def solve():
    """Index: 1734.
    Returns: the total points the team will have after 5 games.
    """
    # L1
    games = 5 # after 5 games
    wade_avg_points_per_game = 20 # His average points per game is 20
    wade_total_points = games * wade_avg_points_per_game

    # L2
    teammates_avg_points_per_game = 40 # his teammates' average points per game is 40
    teammates_total_points = teammates_avg_points_per_game * games

    # L3
    total_team_score = wade_total_points + teammates_total_points

    # FA
    answer = total_team_score
    return answer
def solve():
    """Index: 1225.
    Returns: the average points per game Donovan Mitchell needs for the rest of the season.
    """
    # L1
    current_average_points = 26 # averaging 26 points per game
    games_played = 15 # played 15 games this season
    current_total_points = current_average_points * games_played

    # L2
    goal_average_points = 30 # goal of averaging 30 points per game
    total_games_season = 20 # entire 20 game season
    goal_total_points = goal_average_points * total_games_season

    # L3
    points_needed_remaining_games = goal_total_points - current_total_points

    # L4
    remaining_games = total_games_season - games_played
    average_points_needed = points_needed_remaining_games / remaining_games

    # FA
    answer = average_points_needed
    return answer
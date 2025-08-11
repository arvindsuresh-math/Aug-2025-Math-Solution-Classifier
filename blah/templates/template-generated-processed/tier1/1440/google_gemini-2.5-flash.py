def solve():
    """Index: 1440.
    Returns: the total points Team Soccer Stars had at the end of the season.
    """
    # L1
    won_games = 14 # won 14 games
    lost_games = 2 # lost 2
    won_and_lost_games = won_games + lost_games

    # L2
    total_games_played = 20 # played a total of 20 games
    drew_games = total_games_played - won_and_lost_games

    # L3
    points_per_win = 3 # 3 points for a win
    points_from_wins = won_games * points_per_win

    # L4
    points_per_draw = 1 # 1 point for a draw
    points_from_draws = drew_games * points_per_draw

    # L5
    points_per_loss = 0 # nothing for a loss
    points_from_losses = lost_games * points_per_loss

    # L6
    total_points = points_from_wins + points_from_draws + points_from_losses

    # FA
    answer = total_points
    return answer
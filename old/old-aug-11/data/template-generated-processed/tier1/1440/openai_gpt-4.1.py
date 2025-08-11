def solve():
    """Index: 1440.
    Returns: the total number of points Soccer Stars had at the end of the season.
    """
    # L1
    games_won = 14 # won 14 games
    games_lost = 2 # lost 2
    won_and_lost = games_won + games_lost

    # L2
    total_games = 20 # played a total of 20 games
    games_drawn = total_games - won_and_lost

    # L3
    points_per_win = 3 # earn 3 points for a win
    points_from_wins = games_won * points_per_win

    # L4
    points_per_draw = 1 # 1 point for a draw
    points_from_draws = games_drawn * points_per_draw

    # L5
    points_per_loss = 0 # nothing for a loss
    points_from_losses = games_lost * points_per_loss

    # L6
    total_points = points_from_wins + points_from_draws + points_from_losses

    # FA
    answer = total_points
    return answer
def solve():
    """Index: 2771.
    Returns: the number of games Jeff won.
    """
    # L1
    hours_played = 2 # 2 hours
    minutes_per_hour = 60 # WK
    total_minutes_played = hours_played * minutes_per_hour

    # L2
    minutes_per_point = 5 # every 5 minutes
    total_points_scored = total_minutes_played / minutes_per_point

    # L3
    points_per_game = 8 # scores 8 points
    games_won = total_points_scored / points_per_game

    # FA
    answer = games_won
    return answer
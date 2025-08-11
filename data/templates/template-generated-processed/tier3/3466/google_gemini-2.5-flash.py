def solve():
    """Index: 3466.
    Returns: the number of points the opponent scored.
    """
    # L1
    total_points_previous_games = 720 # scored a total of 720 points
    num_previous_games = 24 # during their previous 24 games
    average_points_previous_games = total_points_previous_games / num_previous_games

    # L2
    half_divisor = 2 # half as much
    half_average_points = average_points_previous_games / half_divisor

    # L3
    points_less_than_half = 2 # 2 points less than half as much
    uf_championship_score = half_average_points - points_less_than_half

    # L4
    opponent_lost_by = 2 # Their opponent only lost by 2 points
    opponent_score = uf_championship_score - opponent_lost_by

    # FA
    answer = opponent_score
    return answer
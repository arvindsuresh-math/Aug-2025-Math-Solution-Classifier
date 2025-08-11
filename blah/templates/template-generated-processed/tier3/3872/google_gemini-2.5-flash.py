def solve():
    """Index: 3872.
    Returns: the points Lola's team needs to score in their next game.
    """
    # L1
    last_home_game_score = 62 # 62 points at their last home game
    half_divisor = 2 # half as many points
    first_away_game_score = last_home_game_score / half_divisor

    # L2
    points_more_second_away = 18 # eighteen points more than the previous away game
    second_away_game_score = first_away_game_score + points_more_second_away

    # L3
    points_more_third_away = 2 # two more points than at their second
    third_away_game_score = second_away_game_score + points_more_third_away

    # L4
    cumulative_multiplier = 4 # four times the score
    goal_cumulative_points = cumulative_multiplier * last_home_game_score

    # Implicit calculation for L5
    current_cumulative_points = last_home_game_score + first_away_game_score + second_away_game_score + third_away_game_score

    # L5
    points_needed_next_game = goal_cumulative_points - current_cumulative_points

    # FA
    answer = points_needed_next_game
    return answer
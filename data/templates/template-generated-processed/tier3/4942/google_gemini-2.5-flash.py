def solve():
    """Index: 4942.
    Returns: the number of points Jessie scored.
    """
    # L1
    total_points_team = 311 # scored a total of 311 points
    points_other_players = 188 # Some players combined for 188 points
    points_lisa_jessie_devin = total_points_team - points_other_players

    # L2
    num_players_equally_scoring = 3 # Lisa, Jessie, and Devin equally scored
    points_per_player = points_lisa_jessie_devin / num_players_equally_scoring

    # L3
    jessie_score = points_per_player

    # FA
    answer = jessie_score
    return answer
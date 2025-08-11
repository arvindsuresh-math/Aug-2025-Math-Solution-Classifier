def solve():
    """Index: 6053.
    Returns: the average points scored by the remaining players.
    """
    # L1
    num_players_first_group = 5 # 5 of them averaged 50 points each
    avg_points_first_group = 50 # 50 points each
    total_points_first_group = num_players_first_group * avg_points_first_group

    # L2
    total_players = 9 # 9 players on the team
    remaining_players = total_players - num_players_first_group

    # L3
    total_team_points = 270 # scored 270 points in the year
    points_remaining_players = total_team_points - total_points_first_group

    # L4
    avg_points_remaining_players = points_remaining_players / remaining_players

    # FA
    answer = avg_points_remaining_players
    return answer
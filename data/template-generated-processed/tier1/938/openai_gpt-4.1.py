def solve():
    """Index: 938.
    Returns: by how many points the first-place team beat Joe's team.
    """
    # L1
    joe_wins = 1 # Joe and his team won 1 game
    points_per_win = 3 # Matches won score 3 points
    joe_win_points = joe_wins * points_per_win

    # L2
    joe_draws = 3 # drew 3
    points_per_draw = 1 # tied matches score 1 point
    joe_draw_points = joe_draws * points_per_draw

    # L3
    joe_total_points = joe_win_points + joe_draw_points

    # L4
    first_place_wins = 2 # first-place team has won 2 games
    first_place_win_points = first_place_wins * points_per_win

    # L5
    first_place_draws = 2 # tied 2
    first_place_draw_points = first_place_draws * points_per_draw

    # L6
    first_place_total_points = first_place_win_points + first_place_draw_points

    # L7
    point_difference = first_place_total_points - joe_total_points

    # FA
    answer = point_difference
    return answer
def solve():
    """Index: 1189.
    Returns: the average number of three-point baskets per game.
    """
    # L1
    total_points_season = 345 # 345 points over the entire season
    total_games = 15 # 15 games over the season
    avg_points_per_game = total_points_season / total_games

    # L2
    two_point_baskets_per_game = 5 # 5 two-point baskets per game
    two_point_value = 2 # two-point baskets
    points_from_two_pointers = two_point_baskets_per_game * two_point_value

    # L3
    free_throws_per_game = 4 # 4 free throws
    free_throw_value = 1 # worth one point
    points_from_free_throws = free_throws_per_game * free_throw_value

    # L4
    points_from_non_three_pointers = points_from_two_pointers + points_from_free_throws

    # L5
    points_from_three_pointers = avg_points_per_game - points_from_non_three_pointers

    # L6
    three_point_value = 3 # three-point baskets
    avg_three_pointers_per_game = points_from_three_pointers / three_point_value

    # FA
    answer = avg_three_pointers_per_game
    return answer
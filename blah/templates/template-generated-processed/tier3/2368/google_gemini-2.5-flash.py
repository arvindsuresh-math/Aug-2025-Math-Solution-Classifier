def solve():
    """Index: 2368.
    Returns: the total points Clayton scored during the first four games.
    """
    # L1
    game1_points = 10 # In the first game, he scored 10 points
    game2_points = 14 # In the second game, he scored 14 points
    game3_points = 6 # In the third game, he scored 6 points
    total_points_first_three_games = game1_points + game2_points + game3_points

    # L2
    number_of_games_for_average = 3 # average of his points from the first three games
    average_points_first_three_games = total_points_first_three_games / number_of_games_for_average

    # L3
    total_points_first_four_games = total_points_first_three_games + average_points_first_three_games

    # FA
    answer = total_points_first_four_games
    return answer
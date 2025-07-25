def solve():
    """Index: 6992.
    Returns: the most total points Tiffany can get.
    """
    # L1
    red_buckets_played = 4 # 4 red buckets
    points_per_red_bucket = 2 # 2 points
    points_from_red_buckets = red_buckets_played * points_per_red_bucket

    # L2
    green_buckets_played = 5 # 5 green buckets
    points_per_green_bucket = 3 # three points
    points_from_green_buckets = green_buckets_played * points_per_green_bucket

    # L3
    games_played = 2 # played two games
    cost_per_play = 1 # Every play costs her $1
    money_spent = games_played * cost_per_play

    # L4
    initial_money = 3 # $3 to play
    money_left = initial_money - money_spent

    # L5
    additional_games_possible = money_left / cost_per_play

    # L7
    rings_per_play = 5 # 5 rings per play
    max_points_final_game = rings_per_play * points_per_green_bucket

    # L8
    total_max_points = points_from_red_buckets + points_from_green_buckets + max_points_final_game

    # FA
    answer = total_max_points
    return answer
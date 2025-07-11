def solve():
    """Index: 1434.
    Returns: the total number of tennis balls used at the end of the tournament.
    """
    # L1
    games_round_1 = 8 # 8 games in the first round
    games_round_2 = 4 # 4 in the second round
    games_round_3 = 2 # 2 in the third round
    games_finals_round = 1 # 1 during the finals
    total_games = games_round_1 + games_round_2 + games_round_3 + games_finals_round

    # L2
    cans_used_per_game = 5 # each game uses 5 cans of tennis balls
    total_cans = total_games * cans_used_per_game

    # L3
    balls_per_can_value = 3 # each can has 3 tennis balls
    total_balls = total_cans * balls_per_can_value

    # FA
    answer = total_balls
    return answer
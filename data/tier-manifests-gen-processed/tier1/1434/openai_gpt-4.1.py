def solve():
    """Index: 1434.
    Returns: the total number of tennis balls used at the end of the tournament.
    """
    # L1
    games_first_round = 8 # 8 games in the first round
    games_second_round = 4 # 4 in the second round
    games_third_round = 2 # 2 in the third round
    games_finals = 1 # 1 during the finals
    total_games = games_first_round + games_second_round + games_third_round + games_finals

    # L2
    cans_per_game = 5 # each game uses 5 cans of tennis balls
    total_cans = total_games * cans_per_game

    # L3
    balls_per_can = 3 # each can has 3 tennis balls
    total_balls = total_cans * balls_per_can

    # FA
    answer = total_balls
    return answer
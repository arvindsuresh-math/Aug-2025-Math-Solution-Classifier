def solve():
    """Index: 3218.
    Returns: the total number of games played by the three friends.
    """
    # L1
    jerry_games = 7 # Jerry won 7 games
    dave_more_than_jerry = 3 # Dave won 3 more games than Jerry
    dave_games = jerry_games + dave_more_than_jerry

    # L2
    ken_more_than_dave = 5 # Ken won 5 more games than Dave
    ken_games = dave_games + ken_more_than_dave

    # L3
    total_games = jerry_games + dave_games + ken_games

    # FA
    answer = total_games
    return answer
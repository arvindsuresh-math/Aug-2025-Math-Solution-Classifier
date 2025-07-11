def solve():
    """Index: 1118.
    Returns: how many more games Perry won than Phil.
    """
    # L1
    phil_won_more_than_charlie = 3 # 3 games more than Charlie
    phil_total_games = 12 # Phil won a total of 12 games
    charlie_won_games = phil_total_games - phil_won_more_than_charlie

    # L2
    charlie_fewer_than_dana = 2 # 2 games fewer than Dana
    dana_won_games = charlie_won_games + charlie_fewer_than_dana

    # L3
    perry_more_than_dana = 5 # five more games than Dana
    perry_won_games = dana_won_games + perry_more_than_dana

    # L4
    perry_more_than_phil = perry_won_games - phil_total_games

    # FA
    answer = perry_more_than_phil
    return answer
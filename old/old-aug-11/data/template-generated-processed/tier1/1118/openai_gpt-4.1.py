def solve():
    """Index: 1118.
    Returns: how many more games Perry won than Phil.
    """
    # L1
    phil_games = 12 # Phil won a total of 12 games
    phil_more_than_charlie = 3 # Phil had won 3 games more than Charlie did
    charlie_games = phil_games - phil_more_than_charlie

    # L2
    charlie_fewer_than_dana = 2 # Charlie had won 2 games fewer than Dana
    dana_games = charlie_games + charlie_fewer_than_dana

    # L3
    perry_more_than_dana = 5 # Perry had won five more games than Dana
    perry_games = dana_games + perry_more_than_dana

    # L4
    perry_more_than_phil = perry_games - phil_games

    # FA
    answer = perry_more_than_phil
    return answer
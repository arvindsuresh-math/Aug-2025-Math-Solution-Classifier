def solve():
    """Index: 3897.
    Returns: the number of ducks at North Pond.
    """
    # L1
    ducks_lake_michigan = 100 # Lake Michigan has 100 ducks
    multiplier_twice = 2 # twice as many ducks
    twice_ducks_lake_michigan = ducks_lake_michigan * multiplier_twice

    # L2
    more_ducks = 6 # Six more
    ducks_north_pond = twice_ducks_lake_michigan + more_ducks

    # FA
    answer = ducks_north_pond
    return answer
def solve():
    """Index: 2326.
    Returns: the number of flowers left in Peter's garden.
    """
    # L1
    amanda_flowers = 20 # Amanda’s garden contains 20 flowers
    multiplier = 3 # three times as many flowers as Amanda's
    peter_initial_flowers = amanda_flowers * multiplier

    # L2
    peter_gave_away = 15 # gave 15 flowers to his brother
    peter_flowers_left = peter_initial_flowers - peter_gave_away

    # FA
    answer = peter_flowers_left
    return answer
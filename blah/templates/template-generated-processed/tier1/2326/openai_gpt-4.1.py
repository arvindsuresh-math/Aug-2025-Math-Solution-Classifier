def solve():
    """Index: 2326.
    Returns: the number of flowers left in Peter's garden after giving 15 to his brother.
    """
    # L1
    amanda_flowers = 20 # Amanda’s garden contains 20 flowers
    peter_multiplier = 3 # Peter’s garden contains three times as many flowers as Amanda's
    peter_flowers = amanda_flowers * peter_multiplier

    # L2
    flowers_given = 15 # Peter gave 15 flowers to his brother
    flowers_left = peter_flowers - flowers_given

    # FA
    answer = flowers_left
    return answer
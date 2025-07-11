def solve():
    """Index: 740.
    Returns: the number of pretzels Angie bought.
    """
    # L1
    barry_pretzels = 12 # If Barry bought 12 pretzels
    shelly_divisor = 2 # half as many pretzels as Barry
    shelly_pretzels = barry_pretzels / shelly_divisor

    # L2
    angie_multiplier = 3 # three times as many pretzels
    angie_pretzels = shelly_pretzels * angie_multiplier

    # FA
    answer = angie_pretzels
    return answer
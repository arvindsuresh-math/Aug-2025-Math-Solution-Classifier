def solve():
    """Index: 3301.
    Returns: the number of frogs Bret caught.
    """
    # L1
    alster_frogs = 2 # Alster who caught 2
    quinn_multiplier = 2 # twice the amount
    quinn_frogs = quinn_multiplier * alster_frogs

    # L2
    bret_multiplier = 3 # three times the amount
    bret_frogs = bret_multiplier * quinn_frogs

    # FA
    answer = bret_frogs
    return answer
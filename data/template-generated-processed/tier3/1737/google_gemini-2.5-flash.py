def solve():
    """Index: 1737.
    Returns: the combined total of minutes Jerry and his friends were in the cold water.
    """
    # L1
    jerry_minutes = 3 # Jerry was in the pool for 3 minutes
    elaine_multiplier = 2 # twice as long as Jerry
    elaine_minutes = elaine_multiplier * jerry_minutes

    # L2
    george_divisor = 3 # one-third as long as Elaine
    george_minutes = elaine_minutes / george_divisor

    # L3
    kramer_minutes = 0 # Kramer, who accidentally locked himself in the bathroom, could not find the pool.

    # L4
    total_minutes = jerry_minutes + elaine_minutes + george_minutes + kramer_minutes

    # FA
    answer = total_minutes
    return answer
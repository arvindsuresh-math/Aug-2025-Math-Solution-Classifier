def solve():
    """Index: 1302.
    Returns: the number of counters and marbles that Reina has (as a tuple: (counters, marbles)).
    """
    # L1
    kevin_counters = 40 # Kevin has 40 counters
    reina_counters_multiplier = 3 # Reina has three times the number of counters
    reina_counters = reina_counters_multiplier * kevin_counters

    # L2
    reina_marbles_multiplier = 4 # Reina has four times the number of marbles
    kevin_marbles = 50 # Kevin has 50 marbles
    reina_marbles = reina_marbles_multiplier * kevin_marbles

    # FA
    answer = (reina_counters, reina_marbles)
    return answer
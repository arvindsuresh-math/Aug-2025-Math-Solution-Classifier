def solve():
    """Index: 1302.
    Returns: the total number of items (counters and marbles) Reina has.
    """
    # L1
    kevin_counters = 40 # 40 counters
    reina_counters_multiplier = 3 # three times the number of counters
    reina_counters = reina_counters_multiplier * kevin_counters

    # L2
    kevin_marbles = 50 # 50 marbles
    reina_marbles_multiplier = 4 # four times the number of marbles
    reina_marbles = reina_marbles_multiplier * kevin_marbles

    # L3
    total_reina_items = reina_counters + reina_marbles

    # FA
    answer = total_reina_items
    return answer
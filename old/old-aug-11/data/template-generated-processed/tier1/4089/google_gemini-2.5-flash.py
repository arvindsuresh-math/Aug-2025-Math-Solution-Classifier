def solve():
    """Index: 4089.
    Returns: the number of peaches Gabrielle has.
    """
    # L3
    martine_total_peaches = 16 # Martine has 16 peaches
    martine_extra_peaches = 6 # 6 more than twice as many peaches
    twice_multiplier = 2 # twice as many peaches
    intermediate_2b = martine_total_peaches - martine_extra_peaches

    # L4
    benjy_peaches = intermediate_2b / twice_multiplier

    # L5
    gabrielle_factor = 3 # Benjy has one-third as many peaches as Gabrielle
    gabrielle_peaches = benjy_peaches * gabrielle_factor

    # FA
    answer = gabrielle_peaches
    return answer
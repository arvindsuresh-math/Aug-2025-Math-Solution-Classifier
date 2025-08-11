def solve():
    """Index: 2399.
    Returns: the number of doubles baseball cards Jess has.
    """
    # L1
    total_rob_cards = 24 # Rob has 24 baseball cards
    rob_doubles_denominator = 3 # One third of Rob's cards
    rob_doubles = total_rob_cards / rob_doubles_denominator

    # L2
    jess_multiplier = 5 # Jess has 5 times as many doubles as Rob
    jess_doubles = rob_doubles * jess_multiplier

    # FA
    answer = jess_doubles
    return answer
def solve():
    """Index: 1179.
    Returns: the total number of baseball cards Rob has.
    """
    # L1
    jess_doubles = 40 # Jess has 40 doubles baseball cards
    jess_multiplier = 5 # Jess has 5 times as many doubles as Rob
    rob_doubles = jess_doubles / jess_multiplier

    # L2
    rob_doubles_fraction_denominator = 3 # One third of Rob's cards are doubles
    total_rob_cards = rob_doubles * rob_doubles_fraction_denominator

    # FA
    answer = total_rob_cards
    return answer
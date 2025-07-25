def solve():
    """Index: 4527.
    Returns: the total money spent by Emma, Elsa, and Elizabeth.
    """
    # L1
    emma_spent = 58 # Emma spent $58
    elsa_multiplier = 2 # twice as much as Emma
    elsa_spent = emma_spent * elsa_multiplier

    # L2
    elizabeth_multiplier = 4 # four times as much as Elsa
    elizabeth_spent = elsa_spent * elizabeth_multiplier

    # L3
    total_spent = emma_spent + elsa_spent + elizabeth_spent

    # FA
    answer = total_spent
    return answer
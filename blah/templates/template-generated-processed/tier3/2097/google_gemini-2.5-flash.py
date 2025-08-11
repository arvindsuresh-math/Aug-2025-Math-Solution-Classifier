def solve():
    """Index: 2097.
    Returns: the amount of money John has.
    """
    # L5
    total_money = 67 # total of $67 in their wallets
    ali_less_than_nada = 5 # Ali has $5 less than Nada
    coefficient_N_combined_terms = 6 # WK
    nada_money = (total_money + ali_less_than_nada) / coefficient_N_combined_terms

    # L6
    john_multiplier = 4 # John has 4 times more than Nada
    john_money = john_multiplier * nada_money

    # FA
    answer = john_money
    return answer
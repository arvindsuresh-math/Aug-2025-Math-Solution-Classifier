def solve():
    """Index: 3531.
    Returns: the amount of money Nigel gave away.
    """
    # L1
    multiplier_twice = 2 # WK
    original_amount = 45 # Nigel won $45
    twice_original_amount = multiplier_twice * original_amount

    # L2
    more_than_twice = 10 # $10 more than twice the amount he originally had
    amount_now = more_than_twice + twice_original_amount

    # L3
    mother_gave = 80 # His mother gave him $80 more
    amount_before_mother = amount_now - mother_gave

    # L4
    amount_given_away = original_amount - amount_before_mother

    # FA
    answer = amount_given_away
    return answer
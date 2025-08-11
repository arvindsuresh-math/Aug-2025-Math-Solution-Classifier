def solve():
    """Index: 4390.
    Returns: the amount less money Jenna has than Bob.
    """
    # L1
    bob_money = 60 # Bob has $60 in his account
    phil_fraction_denominator = 3 # one-third the amount of money
    phil_money = bob_money / phil_fraction_denominator

    # L2
    jenna_multiplier = 2 # twice as much money
    jenna_money = phil_money * jenna_multiplier

    # L3
    money_difference = bob_money - jenna_money

    # FA
    answer = money_difference
    return answer
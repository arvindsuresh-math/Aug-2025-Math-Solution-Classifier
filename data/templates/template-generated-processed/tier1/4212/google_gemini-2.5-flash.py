def solve():
    """Index: 4212.
    Returns: the total amount of money Braden had in his money box after winning the bet.
    """
    # L1
    braden_initial_money = 400 # Braden had $400 in his money box
    multiplier_for_winner = 2 # give the winner twice as much money
    braden_received_from_bet = multiplier_for_winner * braden_initial_money

    # L2
    total_money_after_bet = braden_received_from_bet + braden_initial_money

    # FA
    answer = total_money_after_bet
    return answer
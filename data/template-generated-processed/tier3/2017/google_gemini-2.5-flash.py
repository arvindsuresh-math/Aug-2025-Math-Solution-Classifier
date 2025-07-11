def solve():
    """Index: 2017.
    Returns: the number of $5 bills Jed received as change.
    """
    # L1
    cost_per_game = 15 # Each board game costs $15
    num_games = 6 # buy 6 different board games
    total_cost = cost_per_game * num_games

    # L2
    bill_paid = 100 # paid using a $100 bill
    change_amount = bill_paid - total_cost

    # L3
    bill_denomination = 5 # only $5 bills for his change
    num_bills_received = change_amount / bill_denomination

    # FA
    answer = num_bills_received
    return answer
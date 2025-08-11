def solve():
    """Index: 5637.
    Returns: the amount of change Mrs. Petersons will receive.
    """
    # L1
    num_tumblers = 10 # 10 tumblers
    cost_per_tumbler = 45 # $45 each
    total_cost_tumblers = cost_per_tumbler * num_tumblers

    # L2
    bill_denomination = 100 # $100 bills
    num_bills = 5 # five $100 bills
    amount_paid = bill_denomination * num_bills

    # L3
    change_received = amount_paid - total_cost_tumblers

    # FA
    answer = change_received
    return answer
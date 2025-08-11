def solve():
    """Index: 4492.
    Returns: the amount of change Jane received.
    """
    # L1
    num_skirts = 2 # 2 skirts
    cost_per_skirt = 13 # $13 each
    cost_skirts = cost_per_skirt * num_skirts

    # L2
    num_blouses = 3 # 3 blouses
    cost_per_blouse = 6 # $6 each
    cost_blouses = cost_per_blouse * num_blouses

    # L3
    total_cost = cost_skirts + cost_blouses

    # L4
    amount_paid = 100 # paid the cashier $100
    change_received = amount_paid - total_cost

    # FA
    answer = change_received
    return answer
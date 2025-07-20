def solve():
    """Index: 6537.
    Returns: the amount of money Alice paid for each acorn.
    """
    # L1
    multiplier = 9 # nine times the price
    bob_price = 6000 # Bob paid $6000 for his acorns
    alice_total_cost = multiplier * bob_price

    # L2
    num_acorns_alice = 3600 # Alice purchased 3600 acorns
    cost_per_acorn = alice_total_cost / num_acorns_alice

    # FA
    answer = cost_per_acorn
    return answer
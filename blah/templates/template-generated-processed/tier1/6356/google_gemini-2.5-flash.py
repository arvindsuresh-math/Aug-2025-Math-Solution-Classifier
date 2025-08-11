def solve():
    """Index: 6356.
    Returns: the amount of change Morgan receives.
    """
    # L1
    hamburger_cost = 4 # hamburger for $4
    onion_rings_cost = 2 # onion rings for $2
    smoothie_cost = 3 # smoothie for $3
    total_cost = hamburger_cost + onion_rings_cost + smoothie_cost

    # L2
    payment_amount = 20 # pays with a $20 bill
    change_received = payment_amount - total_cost

    # FA
    answer = change_received
    return answer
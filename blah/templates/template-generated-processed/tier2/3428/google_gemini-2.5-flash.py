def solve():
    """Index: 3428.
    Returns: the total amount Jorge spent on tickets.
    """
    # L1
    num_tickets = 24 # 24 tickets
    price_per_ticket = 7 # $7 each
    total_cost_before_discount = num_tickets * price_per_ticket

    # L2
    discount_factor = 0.50 # discount of 50%
    final_cost = total_cost_before_discount * discount_factor

    # FA
    answer = final_cost
    return answer
def solve():
    """Index: 421.
    Returns: the amount of savings Mrs. Wilsborough has left after buying tickets.
    """
    # L1
    cost_per_vip_ticket = 100 # $100 each
    num_vip_tickets = 2 # 2 VIP tickets
    cost_vip_tickets = cost_per_vip_ticket * num_vip_tickets

    # L2
    cost_per_regular_ticket = 50 # $50 each
    num_regular_tickets = 3 # 3 regular tickets
    cost_regular_tickets = cost_per_regular_ticket * num_regular_tickets

    # L3
    total_ticket_cost = cost_vip_tickets + cost_regular_tickets

    # L4
    initial_savings = 500 # saved $500
    remaining_savings = initial_savings - total_ticket_cost

    # FA
    answer = remaining_savings
    return answer
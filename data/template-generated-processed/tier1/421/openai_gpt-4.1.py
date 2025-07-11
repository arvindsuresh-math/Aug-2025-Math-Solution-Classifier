def solve():
    """Index: 421.
    Returns: the amount of Mrs. Wilsborough's savings left after buying the tickets.
    """
    # L1
    vip_ticket_price = 100 # $100 each (VIP)
    num_vip_tickets = 2 # 2 VIP tickets
    vip_total = vip_ticket_price * num_vip_tickets

    # L2
    regular_ticket_price = 50 # $50 each (regular)
    num_regular_tickets = 3 # 3 regular tickets
    regular_total = regular_ticket_price * num_regular_tickets

    # L3
    total_cost = vip_total + regular_total

    # L4
    initial_savings = 500 # $500 to buy concert tickets
    savings_left = initial_savings - total_cost

    # FA
    answer = savings_left
    return answer
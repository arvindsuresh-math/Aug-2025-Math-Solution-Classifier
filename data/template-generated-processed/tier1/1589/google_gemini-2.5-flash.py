def solve():
    """Index: 1589.
    Returns: the total money made from ticket sales.
    """
    # L1
    matinee_ticket_price = 5 # matinee tickets for $5
    num_matinee_tickets = 200 # 200 matinee tickets
    revenue_matinee = matinee_ticket_price * num_matinee_tickets

    # L2
    evening_ticket_price = 12 # evening tickets for $12
    num_evening_tickets = 300 # 300 evening tickets
    revenue_evening = evening_ticket_price * num_evening_tickets

    # L3
    three_d_ticket_price = 20 # 3D tickets for $20
    num_three_d_tickets = 100 # 100 3D tickets
    revenue_three_d = three_d_ticket_price * num_three_d_tickets

    # L4
    total_revenue = revenue_matinee + revenue_evening + revenue_three_d

    # FA
    answer = total_revenue
    return answer
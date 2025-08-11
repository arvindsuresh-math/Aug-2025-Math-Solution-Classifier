def solve():
    """Index: 1589.
    Returns: the total revenue made from all ticket sales.
    """
    # L1
    matinee_price = 5 # matinee tickets for $5
    matinee_tickets = 200 # sell 200 matinee tickets
    matinee_revenue = matinee_price * matinee_tickets

    # L2
    evening_price = 12 # evening tickets for $12
    evening_tickets = 300 # sell 300 evening tickets
    evening_revenue = evening_price * evening_tickets

    # L3
    d3_price = 20 # 3D tickets for $20
    d3_tickets = 100 # sell 100 3D tickets
    d3_revenue = d3_price * d3_tickets

    # L4
    total_revenue = matinee_revenue + evening_revenue + d3_revenue

    # FA
    answer = total_revenue
    return answer
def solve():
    """Index: 4450.
    Returns: the total amount Jenna's friends pay for their tickets.
    """
    # L1
    normal_ticket_price = 50 # for $50 each
    num_tickets_website = 2 # two of the tickets
    cost_website_tickets = normal_ticket_price * num_tickets_website

    # L2
    scalper_price_percent = 240 # 240% of the normal price
    scalper_price_factor = 2.4 # from solution text: 2.4
    scalper_initial_price = cost_website_tickets * scalper_price_factor

    # L3
    scalper_discount = 10 # $10 off that total payment
    scalper_final_price = scalper_initial_price - scalper_discount

    # L4
    friend_discount_percent = 60 # 60% of the normal price
    friend_discount_factor = 0.6 # from solution text: .6
    cost_friend_ticket = normal_ticket_price * friend_discount_factor

    # L5
    total_cost = cost_website_tickets + scalper_final_price + cost_friend_ticket

    # FA
    answer = total_cost
    return answer
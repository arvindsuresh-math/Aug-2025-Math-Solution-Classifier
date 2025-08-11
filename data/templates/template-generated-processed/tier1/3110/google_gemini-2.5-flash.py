def solve():
    """Index: 3110.
    Returns: the total money needed to buy everyone's tickets.
    """
    # L1
    adult_ticket_price = 11 # Adult tickets are $11
    num_adult_tickets = 2 # her husband, herself
    cost_adult_tickets = adult_ticket_price * num_adult_tickets

    # L2
    senior_ticket_price = 9 # Senior citizen’s tickets (ages 60+) are $9
    num_senior_tickets = 2 # her parents (ages 72 and 75)
    cost_senior_tickets = senior_ticket_price * num_senior_tickets

    # L3
    child_ticket_price = 8 # Children’s tickets (ages 3-12) are $8
    num_child_tickets = 3 # her three children (ages 7, 10, 14) - solution assumes 3 children tickets are bought, despite 14-year-old being outside 3-12 range
    cost_child_tickets = child_ticket_price * num_child_tickets

    # L4
    total_cost = cost_adult_tickets + cost_senior_tickets + cost_child_tickets

    # FA
    answer = total_cost
    return answer
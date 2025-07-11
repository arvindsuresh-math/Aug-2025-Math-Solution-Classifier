def solve():
    """Index: 2443.
    Returns: the amount of change Mary will receive after buying circus tickets.
    """
    # L1
    adult_ticket_price = 2 # Tickets cost $2 for adults
    num_adult_tickets = 1 # Mary (1 adult)
    mary_ticket_cost = adult_ticket_price * num_adult_tickets

    # L2
    num_children = 3 # 3 children
    child_ticket_price = 1 # $1 for children
    children_ticket_cost = num_children * child_ticket_price

    # L3
    total_ticket_cost = mary_ticket_cost + children_ticket_cost

    # L4
    amount_paid = 20 # Mary pays with a $20 bill
    change = amount_paid - total_ticket_cost

    # FA
    answer = change
    return answer
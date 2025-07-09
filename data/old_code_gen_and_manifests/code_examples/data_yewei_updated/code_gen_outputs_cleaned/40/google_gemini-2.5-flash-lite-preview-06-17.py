def solve(
    ticket_cost: int = 40, # A concert ticket costs $40
    tickets_bought: int = 12, # Mr. Benson bought 12 tickets
    discount_threshold: int = 10, # for every ticket bought that exceeds 10
    discount_rate: float = 0.05 # received a 5% discount
):
    """Index: 40.
    Returns: the total amount Mr. Benson paid for the tickets.
    """
    #: L1
    discounted_tickets_count = tickets_bought - discount_threshold

    #: L2
    discount_per_ticket = ticket_cost * discount_rate

    #: L3
    discounted_ticket_cost = ticket_cost - discount_per_ticket

    #: L4
    cost_of_discounted_tickets = discounted_ticket_cost * discounted_tickets_count

    #: L5
    cost_of_full_price_tickets = ticket_cost * (tickets_bought - discounted_tickets_count)

    #: L6
    total_cost = cost_of_full_price_tickets + cost_of_discounted_tickets

    answer = total_cost # FINAL ANSWER
    return answer
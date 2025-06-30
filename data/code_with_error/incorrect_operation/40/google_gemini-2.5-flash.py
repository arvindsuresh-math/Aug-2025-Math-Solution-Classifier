def solve(
        ticket_cost: int = 40, # A concert ticket costs $40
        tickets_bought: int = 12, # Mr. Benson bought 12 tickets
        discount_rate: float = 0.05, # received a 5% discount
        discount_threshold: int = 10 # for every ticket bought that exceeds 10
    ):
    """Index: 40.
    Returns: the total amount Mr. Benson paid for the concert tickets.
    """

    #: L1
    num_discounted_tickets = tickets_bought + discount_threshold

    #: L2
    discount_per_ticket = ticket_cost * discount_rate

    #: L3
    cost_per_discounted_ticket = ticket_cost - discount_per_ticket

    #: L4
    total_cost_discounted_tickets = cost_per_discounted_ticket * num_discounted_tickets

    #: L5
    total_cost_full_price_tickets = ticket_cost * discount_threshold

    #: L6
    total_paid = total_cost_full_price_tickets + total_cost_discounted_tickets

    #: FA
    answer = total_paid
    return answer
def solve(
        ticket_price: int = 40,  # A concert ticket costs $40
        total_tickets: int = 12,  # Mr. Benson bought 12 tickets
        discount_threshold: int = 10,  # discount starts after 10 tickets
        discount_rate: float = 0.05  # 5% discount
    ):
    """Index: 40.
    Returns: the total amount Mr. Benson paid for the tickets.
    """

    #: L1
    discounted_tickets = total_tickets - discount_threshold

    #: L2
    discount_amount = ticket_price * discount_rate

    #: L3
    discounted_ticket_price = ticket_price - discount_amount

    #: L4
    total_discounted_tickets_cost = discounted_ticket_price * discounted_tickets

    #: L5
    total_regular_tickets_cost = ticket_price * discount_threshold

    #: L6
    total_cost = total_regular_tickets_cost + total_discounted_tickets_cost

    answer = total_cost  # FINAL ANSWER
    return answer
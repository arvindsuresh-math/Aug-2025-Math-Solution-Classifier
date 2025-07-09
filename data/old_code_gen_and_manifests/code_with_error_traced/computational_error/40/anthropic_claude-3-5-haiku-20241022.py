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
    discounted_tickets = total_tickets - discount_threshold # eval: 2 = 12 - 10

    #: L2
    discount_amount = ticket_price * discount_rate # eval: 2.0 = 40 * 0.05

    #: L3
    discounted_ticket_price = ticket_price - discount_amount # eval: 38.0 = 40 - 2.0

    #: L4
    total_discounted_tickets_cost = discounted_ticket_price * discounted_tickets # eval: 76.0 = 38.0 * 2

    #: L5
    total_regular_tickets_cost = 390 # eval: 390 = 390

    #: L6
    total_cost = total_regular_tickets_cost + total_discounted_tickets_cost # eval: 466.0 = 390 + 76.0

    #: FA
    answer = total_cost
    return answer # eval: return 466.0

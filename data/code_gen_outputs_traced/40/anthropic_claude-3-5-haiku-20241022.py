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
    total_regular_tickets_cost = ticket_price * discount_threshold # eval: 400 = 40 * 10
    #: L6
    total_cost = total_regular_tickets_cost + total_discounted_tickets_cost # eval: 476.0 = 400 + 76.0
    answer = total_cost  # FINAL ANSWER # eval: 476.0 = 476.0  # FINAL ANSWER
    return answer # eval: return 476.0
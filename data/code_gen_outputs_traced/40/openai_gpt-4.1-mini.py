def solve(
    ticket_price: int = 40,  # A concert ticket costs $40
    tickets_bought: int = 12,  # Mr. Benson bought 12 tickets
    discount_rate: float = 0.05,  # 5% discount for every ticket bought that exceeds 10
    discount_threshold: int = 10  # discount applies for tickets exceeding 10
):
    """Index: 40.
    Returns: the total amount Mr. Benson paid for the tickets after discount.
    """
    #: L1
    discounted_tickets = tickets_bought - discount_threshold # eval: 2 = 12 - 10
    #: L2
    discount_per_ticket = ticket_price * discount_rate # eval: 2.0 = 40 * 0.05
    #: L3
    discounted_ticket_price = ticket_price - discount_per_ticket # eval: 38.0 = 40 - 2.0
    #: L4
    total_discounted_tickets_cost = discounted_ticket_price * discounted_tickets # eval: 76.0 = 38.0 * 2
    #: L5
    full_price_tickets = discount_threshold # eval: 10 = 10
    total_full_price_tickets_cost = ticket_price * full_price_tickets # eval: 400 = 40 * 10
    #: L6
    total_cost = total_full_price_tickets_cost + total_discounted_tickets_cost # eval: 476.0 = 400 + 76.0
    answer = total_cost  # FINAL ANSWER # eval: 476.0 = 476.0  # FINAL ANSWER
    return answer # eval: return 476.0
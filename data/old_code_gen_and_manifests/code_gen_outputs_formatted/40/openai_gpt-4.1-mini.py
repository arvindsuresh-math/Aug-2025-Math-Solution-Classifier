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
    discounted_tickets = tickets_bought - discount_threshold

    #: L2
    discount_per_ticket = ticket_price * discount_rate

    #: L3
    discounted_ticket_price = ticket_price - discount_per_ticket

    #: L4
    total_discounted_tickets_cost = discounted_ticket_price * discounted_tickets

    #: L5
    full_price_tickets = discount_threshold
    total_full_price_tickets_cost = ticket_price * full_price_tickets

    #: L6
    total_cost = total_full_price_tickets_cost + total_discounted_tickets_cost

    #: FA
    answer = total_cost
    return answer
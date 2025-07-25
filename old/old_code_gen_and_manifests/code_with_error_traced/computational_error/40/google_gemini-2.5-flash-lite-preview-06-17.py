def solve(
    ticket_price: int = 40, # A concert ticket costs $40
    tickets_bought: int = 12, # Mr. Benson bought 12 tickets
    discount_threshold: int = 10, # for every ticket bought that exceeds 10
    discount_rate: float = 0.05 # received a 5% discount
):
    """Index: 40.
    Returns: the total amount Mr. Benson paid for the tickets.
    """

    #: L1
    discountable_tickets = tickets_bought - discount_threshold # eval: 2 = 12 - 10

    #: L2
    discount_per_ticket = ticket_price * discount_rate # eval: 2.0 = 40 * 0.05

    #: L3
    discounted_ticket_price = ticket_price - discount_per_ticket # eval: 38.0 = 40 - 2.0

    #: L4
    cost_of_discounted_tickets = 86.0 # eval: 86.0 = 86.0

    #: L5
    cost_of_full_price_tickets = ticket_price * discountable_tickets # eval: 80 = 40 * 2

    #: L6
    total_cost = cost_of_full_price_tickets + cost_of_discounted_tickets # eval: 166.0 = 80 + 86.0

    #: FA
    answer = total_cost
    return answer # eval: return 166.0

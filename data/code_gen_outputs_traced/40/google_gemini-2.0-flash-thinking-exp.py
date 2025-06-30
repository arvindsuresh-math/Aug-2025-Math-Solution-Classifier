def solve(
    ticket_cost: int = 40, # A concert ticket costs $40
    tickets_bought: int = 12, # Mr. Benson bought 12 tickets
    discount_rate: float = 0.05, # received a 5% discount
    discount_threshold: int = 10 # for every ticket bought that exceeds 10
):
    """Index: 40.
    Returns: the total amount Mr. Benson paid for the tickets.
    """
    #: L1
    num_discounted_tickets = tickets_bought - discount_threshold # eval: 2 = 12 - 10
    #: L2
    discount_amount_per_ticket = ticket_cost * discount_rate # eval: 2.0 = 40 * 0.05
    #: L3
    cost_per_discounted_ticket = ticket_cost - discount_amount_per_ticket # eval: 38.0 = 40 - 2.0
    #: L4
    total_cost_discounted_tickets = cost_per_discounted_ticket * num_discounted_tickets # eval: 76.0 = 38.0 * 2
    #: L5
    num_full_price_tickets = discount_threshold # eval: 10 = 10
    total_cost_full_price_tickets = ticket_cost * num_full_price_tickets # eval: 400 = 40 * 10
    #: L6
    total_paid = total_cost_full_price_tickets + total_cost_discounted_tickets # eval: 476.0 = 400 + 76.0
    answer = total_paid # FINAL ANSWER # eval: 476.0 = 476.0 # FINAL ANSWER
    return answer # eval: return 476.0
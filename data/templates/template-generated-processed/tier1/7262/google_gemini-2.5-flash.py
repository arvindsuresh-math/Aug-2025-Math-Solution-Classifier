def solve():
    """Index: 7262.
    Returns: the total amount he paid for the tickets.
    """
    # L1
    ticket_price_per_person = 44 # $44 per person
    num_people = 3 # his parents and himself
    cost_tickets = ticket_price_per_person * num_people

    # L2
    service_fee = 18 # an $18 service fee
    total_amount_paid = cost_tickets + service_fee

    # FA
    answer = total_amount_paid
    return answer
def solve():
    """Index: 2190.
    Returns: the amount of money the group of six friends lost.
    """
    # L1
    ticket_cost = 50 # $50 for the ticket
    entree_cost = 10 # $10 for their entrée
    per_person_cost = ticket_cost + entree_cost

    # L2
    num_people = 6 # Jenny and 5 friends
    total_ticket_entree_cost = per_person_cost * num_people

    # L3
    drink_ticket_divisor = 2 # half the people
    num_drink_tickets = num_people / drink_ticket_divisor

    # L4
    drink_ticket_cost = 30 # $30/person for unlimited drink tickets
    total_drink_ticket_cost = num_drink_tickets * drink_ticket_cost

    # L5
    total_evening_cost = total_drink_ticket_cost + total_ticket_entree_cost

    # L6
    refund_percent = 0.9 # 90% refund
    refund_amount = total_evening_cost * refund_percent

    # L7
    money_lost = total_evening_cost - refund_amount

    # FA
    answer = money_lost
    return answer
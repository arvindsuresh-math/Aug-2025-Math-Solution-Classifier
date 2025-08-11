def solve():
    """Index: 2190.
    Returns: the amount of money the group of six friends lost.
    """
    # L1
    ticket_cost_per_person = 50 # $50 for the ticket
    entree_cost_per_person = 10 # $10 for their entrée
    cost_per_person_ticket_entree = ticket_cost_per_person + entree_cost_per_person

    # L2
    num_people = 6 # group of six friends
    total_cost_ticket_entree = cost_per_person_ticket_entree * num_people

    # L3
    drink_ticket_half_divisor = 2 # half the people
    num_people_with_drink_tickets = num_people / drink_ticket_half_divisor

    # L4
    drink_ticket_cost_per_person = 30 # $30/person
    total_cost_drink_tickets = num_people_with_drink_tickets * drink_ticket_cost_per_person

    # L5
    total_cost_evening = total_cost_drink_tickets + total_cost_ticket_entree

    # L6
    refund_percent = 0.9 # 90% refund
    refund_amount = total_cost_evening * refund_percent

    # L7
    money_lost = total_cost_evening - refund_amount

    # FA
    answer = money_lost
    return answer
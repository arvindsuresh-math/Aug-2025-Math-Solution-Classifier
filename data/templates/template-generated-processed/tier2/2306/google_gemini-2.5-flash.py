def solve():
    """Index: 2306.
    Returns: the total amount spent on movie tickets after discount.
    """
    # L1
    children_ticket_cost = 4.25 # Children’s tickets cost $4.25
    adult_ticket_markup = 3.25 # adult tickets cost $3.25 more
    adult_ticket_cost = children_ticket_cost + adult_ticket_markup

    # L2
    num_adult_tickets = 2 # two adult tickets
    total_adult_tickets_cost = adult_ticket_cost * num_adult_tickets

    # L3
    num_children_tickets = 4 # four children’s tickets
    total_children_tickets_cost = children_ticket_cost * num_children_tickets

    # L4
    subtotal_tickets_cost = total_adult_tickets_cost + total_children_tickets_cost

    # L5
    discount_amount = 2 # $2 discount
    final_cost = subtotal_tickets_cost - discount_amount

    # FA
    answer = final_cost
    return answer
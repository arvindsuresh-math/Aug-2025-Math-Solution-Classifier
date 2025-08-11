def solve():
    """Index: 5079.
    Returns: the total amount Connor will spend on his date.
    """
    # L1
    ticket_cost_per_person = 10.00 # The tickets cost $10.00 each
    num_tickets = 2 # buy 2 tickets
    total_ticket_cost = ticket_cost_per_person * num_tickets

    # L2
    num_candy_boxes = 2 # each grab a box of candy
    candy_cost_per_box = 2.50 # $2.50 each
    total_candy_cost = num_candy_boxes * candy_cost_per_box

    # L3
    combo_meal_cost = 11.00 # combo meal for $11.00
    total_spend = total_ticket_cost + total_candy_cost + combo_meal_cost

    # FA
    answer = total_spend
    return answer
def solve():
    """Index: 2306.
    Returns: the total amount Ashley and her family spent on movie tickets after discount.
    """
    # L1
    child_ticket_price = 4.25 # Children’s tickets cost $4.25
    adult_ticket_extra = 3.25 # adult tickets cost $3.25 more
    adult_ticket_price = child_ticket_price + adult_ticket_extra

    # L2
    num_adult_tickets = 2 # two adult tickets
    adult_tickets_total = adult_ticket_price * num_adult_tickets

    # L3
    num_child_tickets = 4 # four children’s tickets
    child_tickets_total = num_child_tickets * child_ticket_price

    # L4
    total_before_discount = adult_tickets_total + child_tickets_total

    # L5
    discount = 2 # $2 discount for buying more than 3 tickets
    total_after_discount = total_before_discount - discount

    # FA
    answer = total_after_discount
    return answer
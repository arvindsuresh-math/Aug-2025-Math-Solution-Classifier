def solve():
    """Index: 1711.
    Returns: the total amount Janet paid for everything.
    """
    # L1
    total_people = 10 # Janet gets tickets for 10 people
    num_children = 4 # 4 of them are children
    num_adults = total_people - num_children

    # L2
    adult_ticket_price = 30 # $30 for admission
    adult_tickets_cost = num_adults * adult_ticket_price

    # L3
    child_ticket_price = adult_ticket_price / 2

    # L4
    children_tickets_cost = child_ticket_price * num_children

    # L5
    total_ticket_cost = children_tickets_cost + adult_tickets_cost

    # L6
    discount_percent = 0.2 # 20% off the total price of admission
    discount_amount = total_ticket_cost * discount_percent

    # L7
    discounted_ticket_cost = total_ticket_cost - discount_amount

    # L8
    soda_price = 5 # buys a soda for $5
    total_paid = discounted_ticket_cost + soda_price

    # FA
    answer = total_paid
    return answer
def solve():
    """Index: 1711.
    Returns: the total amount Janet paid.
    """
    # L1
    total_people = 10 # 10 people
    num_children = 4 # 4 of them are children
    num_adult_tickets = total_people - num_children

    # L2
    admission_price = 30 # $30 for admission
    cost_adult_tickets = num_adult_tickets * admission_price

    # L3
    children_discount_divisor = 2 # half price
    cost_per_child_ticket = admission_price / children_discount_divisor

    # L4
    cost_children_tickets = cost_per_child_ticket * num_children

    # L5
    total_ticket_cost_before_discount = cost_children_tickets + cost_adult_tickets

    # L6
    discount_percent = 0.2 # 20% off
    discount_amount = total_ticket_cost_before_discount * discount_percent

    # L7
    total_ticket_cost_after_discount = total_ticket_cost_before_discount - discount_amount

    # L8
    soda_cost = 5 # soda for $5
    total_paid = total_ticket_cost_after_discount + soda_cost

    # FA
    answer = total_paid
    return answer
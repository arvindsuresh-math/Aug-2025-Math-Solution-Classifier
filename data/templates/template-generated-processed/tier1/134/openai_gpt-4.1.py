def solve():
    """Index: 134.
    Returns: the amount of change the family will receive after paying for tickets.
    """
    # L1
    regular_ticket_price = 109 # regular ticket costs $109
    child_discount = 5 # children below 12 years old have a $5 discount
    child_ticket_price = regular_ticket_price - child_discount

    # L2
    num_children = 2 # two children
    total_child_tickets = child_ticket_price * num_children

    # L3
    num_adults = 2 # couple
    total_adult_tickets = regular_ticket_price * num_adults

    # L4
    total_payment = total_child_tickets + total_adult_tickets

    # L5
    cash_given = 500 # they gave the cashier $500
    change = cash_given - total_payment

    # FA
    answer = change
    return answer
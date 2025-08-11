def solve():
    """Index: 2443.
    Returns: the amount of change Mary will receive.
    """
    # L1
    adult_ticket_price = 2 # $2 for adults
    num_adult_tickets = 1 # Mary goes with her children (implies she is one adult)
    mary_ticket_cost = adult_ticket_price * num_adult_tickets

    # L2
    num_children_tickets = 3 # 3 children
    child_ticket_price = 1 # $1 for children
    children_total_cost = num_children_tickets * child_ticket_price

    # L3
    total_tickets_cost = mary_ticket_cost + children_total_cost

    # L4
    bill_amount = 20 # $20 bill
    change_amount = bill_amount - total_tickets_cost

    # FA
    answer = change_amount
    return answer
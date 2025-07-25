def solve():
    """Index: 2677.
    Returns: the cost of one child's ticket.
    """
    # L1
    num_adults = 10 # Ten adults
    adult_ticket_price = 8 # Adult tickets are $8 each
    total_adult_cost = num_adults * adult_ticket_price

    # L2
    total_bill = 124 # the total bill was $124
    total_children_cost = total_bill - total_adult_cost

    # L3
    num_children = 11 # eleven children
    child_ticket_price = total_children_cost / num_children

    # FA
    answer = child_ticket_price
    return answer
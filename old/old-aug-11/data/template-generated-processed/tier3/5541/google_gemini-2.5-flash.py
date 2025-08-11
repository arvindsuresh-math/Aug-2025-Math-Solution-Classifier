def solve():
    """Index: 5541.
    Returns: the cost per adult ticket in dollars.
    """
    # L1
    total_cost = 76 # The total cost of their trip is $76
    concessions_cost = 12 # buy $12 worth of concessions
    cost_for_tickets = total_cost - concessions_cost

    # L2
    child_ticket_cost = 7 # each child's ticket is $7
    num_children = 2 # two children
    total_child_tickets_cost = child_ticket_cost * num_children

    # L3
    total_adult_tickets_cost = cost_for_tickets - total_child_tickets_cost

    # L4
    num_adults = 5 # Five adults
    cost_per_adult_ticket = total_adult_tickets_cost / num_adults

    # FA
    answer = cost_per_adult_ticket
    return answer
def solve():
    """Index: 2737.
    Returns: the total money the zoo made for both days.
    """
    # L1
    children_monday = 7 # 7 children
    children_tuesday = 4 # 4 children
    total_children = children_monday + children_tuesday

    # L2
    child_ticket_cost = 3 # Child tickets cost $3
    cost_children_tickets = total_children * child_ticket_cost

    # L3
    adults_monday = 5 # 5 adults
    adults_tuesday = 2 # 2 adults
    total_adults = adults_monday + adults_tuesday

    # L4
    adult_ticket_cost = 4 # adult tickets cost $4
    cost_adult_tickets = total_adults * adult_ticket_cost

    # L5
    total_money_made = cost_children_tickets + cost_adult_tickets

    # FA
    answer = total_money_made
    return answer
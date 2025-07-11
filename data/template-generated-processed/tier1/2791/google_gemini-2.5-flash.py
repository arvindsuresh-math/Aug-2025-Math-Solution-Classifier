def solve():
    """Index: 2791.
    Returns: the total cost if Violet buys separate tickets.
    """
    # L1
    num_children = 6 # 6 children
    cost_per_child_ticket = 20 # children's tickets cost $20
    total_children_cost = num_children * cost_per_child_ticket

    # L2
    cost_adult_ticket = 35 # adult tickets cost $35
    total_separate_tickets_cost = total_children_cost + cost_adult_ticket

    # FA
    answer = total_separate_tickets_cost
    return answer
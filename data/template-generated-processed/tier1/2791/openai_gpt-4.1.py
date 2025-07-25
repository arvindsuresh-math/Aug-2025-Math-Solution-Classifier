def solve():
    """Index: 2791.
    Returns: the total cost if Violet buys separate tickets for her family.
    """
    # L1
    num_children = 6 # Violet's family has 6 children
    child_ticket_price = 20 # children's tickets cost $20
    children_total = num_children * child_ticket_price

    # L2
    adult_ticket_price = 35 # adult tickets cost $35
    total_cost = children_total + adult_ticket_price

    # FA
    answer = total_cost
    return answer
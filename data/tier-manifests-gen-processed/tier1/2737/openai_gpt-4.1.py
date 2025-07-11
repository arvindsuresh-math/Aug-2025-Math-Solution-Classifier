def solve():
    """Index: 2737.
    Returns: the total amount of money the zoo made in ticket sales for both days.
    """
    # L1
    children_monday = 7 # 7 children ... on Monday
    children_tuesday = 4 # 4 children ... on Tuesday
    total_children = children_monday + children_tuesday

    # L2
    child_ticket_cost = 3 # Child tickets cost $3
    total_child_ticket_revenue = total_children * child_ticket_cost

    # L3
    adults_monday = 5 # 5 adults ... on Monday
    adults_tuesday = 2 # 2 adults ... on Tuesday
    total_adults = adults_monday + adults_tuesday

    # L4
    adult_ticket_cost = 4 # adult tickets cost $4
    total_adult_ticket_revenue = total_adults * adult_ticket_cost

    # L5
    total_revenue = total_child_ticket_revenue + total_adult_ticket_revenue

    # FA
    answer = total_revenue
    return answer
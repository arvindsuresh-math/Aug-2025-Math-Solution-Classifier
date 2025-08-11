def solve():
    """Index: 5494.
    Returns: the number of children the adult can take to the movies.
    """
    # L2
    total_money = 35 # She has $35
    adult_ticket_cost = 8 # A movie ticket for an adult costs $8
    money_for_children = total_money - adult_ticket_cost

    # L3
    child_ticket_cost = 3 # a child's ticket costs $3
    num_children = money_for_children / child_ticket_cost

    # FA
    answer = num_children
    return answer
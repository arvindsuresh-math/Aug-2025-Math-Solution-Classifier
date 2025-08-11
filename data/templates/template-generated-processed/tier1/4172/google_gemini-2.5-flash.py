def solve():
    """Index: 4172.
    Returns: the dollar difference in cost between adult and children's tickets.
    """
    # L1
    num_adults = 9 # Nine adults
    adult_ticket_price = 11 # $11 each
    total_adult_cost = num_adults * adult_ticket_price

    # L2
    num_children = 7 # seven children
    child_ticket_price = 7 # $7 each
    total_child_cost = num_children * child_ticket_price

    # L3
    cost_difference = total_adult_cost - total_child_cost

    # FA
    answer = cost_difference
    return answer
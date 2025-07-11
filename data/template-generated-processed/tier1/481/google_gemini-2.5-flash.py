def solve():
    """Index: 481.
    Returns: the total cost for the tickets.
    """
    # L1
    adult_ticket_price = 12 # $12 for adults
    num_adults = 3 # her mom, dad, grandma
    cost_adults = adult_ticket_price * num_adults

    # L2
    child_ticket_price = 10 # $10 for children
    num_children = 3 # three little sisters
    cost_children = child_ticket_price * num_children

    # L3
    total_cost = cost_adults + cost_children

    # FA
    answer = total_cost
    return answer
def solve():
    """Index: 481.
    Returns: the total cost for the family's tickets to the show.
    """
    # L1
    adult_ticket_price = 12 # Tickets are $12 for adults
    num_adults = 3 # mom, dad, grandma
    adult_total = adult_ticket_price * num_adults

    # L2
    child_ticket_price = 10 # $10 for children
    num_children = 3 # three little sisters
    child_total = child_ticket_price * num_children

    # L3
    total_cost = adult_total + child_total

    # FA
    answer = total_cost
    return answer
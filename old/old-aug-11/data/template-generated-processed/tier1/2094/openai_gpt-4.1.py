def solve():
    """Index: 2094.
    Returns: the total price the family will pay for admission.
    """
    # L3
    adult_ticket_price = 22 # adult tickets cost $22 for admission
    num_adults = 2 # family consists of 2 adults
    child_ticket_price = 7 # tickets for children cost $7
    num_children = 2 # family consists of 2 children
    total_price = adult_ticket_price * num_adults + child_ticket_price * num_children

    # FA
    answer = total_price
    return answer
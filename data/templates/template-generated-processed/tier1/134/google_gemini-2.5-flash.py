def solve():
    """Index: 134.
    Returns: the amount of change the family will receive.
    """
    # L1
    regular_ticket_cost = 109 # The regular ticket costs $109
    child_discount = 5 # children below 12 years old have a $5 discount
    child_ticket_cost = regular_ticket_cost - child_discount

    # L2
    num_children = 2 # two children
    total_child_cost = child_ticket_cost * num_children

    # L3
    num_adults = 2 # A couple
    total_adult_cost = regular_ticket_cost * num_adults

    # L4
    total_family_cost = total_child_cost + total_adult_cost

    # L5
    amount_given_cashier = 500 # If they gave the cashier $500
    change_received = amount_given_cashier - total_family_cost

    # FA
    answer = change_received
    return answer
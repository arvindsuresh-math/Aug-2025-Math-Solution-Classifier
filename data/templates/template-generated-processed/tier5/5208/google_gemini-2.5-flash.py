def solve():
    """Index: 5208.
    Returns: the number of children in the group.
    """
    # L4
    adult_ticket_price = 15 # The price of an adult ticket is $15
    more_adults_than_children = 25 # 25 more adults than children
    total_cost = 720 # A group of people pays $720 for admission tickets
    adult_cost_constant_part = adult_ticket_price * more_adults_than_children

    # L5
    child_ticket_price = 8 # a child ticket is $8
    coefficient_of_X = child_ticket_price + adult_ticket_price

    # L6
    rhs_after_subtraction = total_cost - adult_cost_constant_part

    # L7
    num_children = rhs_after_subtraction / coefficient_of_X

    # FA
    answer = num_children
    return answer
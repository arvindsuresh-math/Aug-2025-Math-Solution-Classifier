def solve():
    """Index: 5406.
    Returns: the cost of an adult ticket.
    """
    # L1 - Let X be the cost of an adult ticket.
    # L2 - So the cost of a child ticket is X-6.
    cost_difference = 6 # cost of an adult ticket is $6 more than the cost of a child ticket

    # L3 - The total cost of the 5 tickets is X*2 + 3*(X-6) = 77.
    num_adults = 2 # Mr. and Mrs. Boyden
    num_children = 3 # 3 children
    total_given_cost = 77 # total cost of the 5 tickets is $77

    # L4 - X*2 + 3*X - 3*6 = 77.
    term_product_children_cost_diff = num_children * cost_difference

    # L5 - 5*X - 18 = 77.
    combined_x_coefficient = num_adults + num_children

    # L6
    sum_on_rhs = total_given_cost + term_product_children_cost_diff

    # L7
    adult_ticket_cost = sum_on_rhs / combined_x_coefficient

    # FA
    answer = adult_ticket_cost
    return answer
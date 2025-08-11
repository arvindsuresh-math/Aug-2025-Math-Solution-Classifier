def solve():
    """Index: 4345.
    Returns: the number of children in the family.
    """
    # L1
    bill_denomination = 20 # two $20 bills
    num_bills = 2 # two $20 bills
    total_given_to_cashier = bill_denomination * num_bills

    # L2
    change_returned = 1 # a $1 change was returned
    total_ticket_cost = total_given_to_cashier - change_returned

    # L3
    regular_ticket_cost = 9 # The regular ticket costs $9
    num_adults = 2 # 2 adults in the family
    adult_ticket_cost = regular_ticket_cost * num_adults

    # L4
    children_ticket_total_cost = total_ticket_cost - adult_ticket_cost

    # L5
    child_ticket_discount = 2 # the ticket for children is $2 less
    cost_per_child_ticket = regular_ticket_cost - child_ticket_discount

    # L6
    num_children = children_ticket_total_cost / cost_per_child_ticket

    # FA
    answer = num_children
    return answer
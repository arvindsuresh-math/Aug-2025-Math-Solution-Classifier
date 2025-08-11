def solve():
    """Index: 7068.
    Returns: the amount of money James has left.
    """
    # L1
    cost_first_two_tickets = 150 # The first 2 cost $150 each
    third_ticket_divisor = 3 # the third cost 1/3 as much
    cost_third_ticket = cost_first_two_tickets / third_ticket_divisor

    # L2
    num_first_two_tickets = 2 # The first 2 cost $150 each
    total_tickets_cost = cost_first_two_tickets * num_first_two_tickets + cost_third_ticket

    # L3
    roommate_share_divisor = 2 # pay half the cost
    james_paid_cost = total_tickets_cost / roommate_share_divisor

    # L4
    initial_bank_balance = 500 # he had $500 in the bank
    money_left_over = initial_bank_balance - james_paid_cost

    # FA
    answer = money_left_over
    return answer
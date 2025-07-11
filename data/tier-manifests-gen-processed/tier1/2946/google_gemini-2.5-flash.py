def solve():
    """Index: 2946.
    Returns: the amount of change the sisters will receive after buying tickets.
    """
    # L1
    ticket_cost_per_person = 8 # $8 per person
    num_sisters = 2 # Two sisters
    total_ticket_cost = ticket_cost_per_person * num_sisters

    # L2
    money_brought = 25 # brought $25 with them
    change_received = money_brought - total_ticket_cost

    # FA
    answer = change_received
    return answer
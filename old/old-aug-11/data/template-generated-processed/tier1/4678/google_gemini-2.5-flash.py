def solve():
    """Index: 4678.
    Returns: the total money the show made.
    """
    # L1
    initial_tickets = 200 # 200 people buy tickets
    multiplier_second_show = 3 # three times as many people show up
    second_show_tickets = initial_tickets * multiplier_second_show

    # L2
    total_tickets_sold = initial_tickets + second_show_tickets

    # L3
    ticket_cost = 25 # each ticket cost $25
    total_money_made = total_tickets_sold * ticket_cost

    # FA
    answer = total_money_made
    return answer
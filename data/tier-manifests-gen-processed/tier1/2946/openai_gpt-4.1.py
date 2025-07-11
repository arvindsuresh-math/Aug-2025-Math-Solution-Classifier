def solve():
    """Index: 2946.
    Returns: the amount of change the sisters will receive after buying the tickets.
    """
    # L1
    ticket_price = 8 # $8 per person
    num_people = 2 # Two sisters
    total_ticket_cost = ticket_price * num_people

    # L2
    money_brought = 25 # $25 with them
    change = money_brought - total_ticket_cost

    # FA
    answer = change
    return answer
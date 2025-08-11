def solve():
    """Index: 3485.
    Returns: the amount of money Maria has left.
    """
    # L1
    ticket_cost = 300 # $300 for the ticket
    hotel_cost_divisor = 2 # half of that for the hotel
    hotel_cost = ticket_cost / hotel_cost_divisor

    # L2
    initial_money = 760 # she had $760 at the beginning
    money_left = initial_money - ticket_cost - hotel_cost

    # FA
    answer = money_left
    return answer
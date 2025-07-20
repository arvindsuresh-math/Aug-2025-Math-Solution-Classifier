def solve():
    """Index: 3131.
    Returns: the total amount George paid for the movie theater visit.
    """
    # L1
    ticket_price = 16 # paid $16 for the ticket
    nachos_divisor = 2 # half the price of the ticket
    nachos_cost = ticket_price / nachos_divisor

    # L2
    total_cost = nachos_cost + ticket_price

    # FA
    answer = total_cost
    return answer
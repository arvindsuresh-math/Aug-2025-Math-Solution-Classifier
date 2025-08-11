def solve():
    """Index: 7190.
    Returns: the amount of money lost by not selling out.
    """
    # L1
    capacity = 50 # can hold 50 people
    ticket_price = 8.00 # charge $8.00 a ticket
    sold_out_revenue = capacity * ticket_price

    # L2
    tickets_sold_tuesday = 24 # only sold 24 tickets
    tuesday_revenue = tickets_sold_tuesday * ticket_price

    # L3
    money_lost = sold_out_revenue - tuesday_revenue

    # FA
    answer = money_lost
    return answer
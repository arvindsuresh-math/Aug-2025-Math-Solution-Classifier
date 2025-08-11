from fractions import Fraction

def solve():
    """Index: 3047.
    Returns: the total earnings from the play.
    """
    # L1
    num_rows = 20 # 20 rows
    seats_per_row = 10 # each row has 10 seats
    total_seats = num_rows * seats_per_row

    # L2
    fraction_sold = Fraction(3, 4) # 3/4 of the seats were sold
    seats_sold = total_seats * fraction_sold

    # L3
    ticket_cost = 10 # ticket costs $10
    total_earnings = ticket_cost * seats_sold

    # FA
    answer = total_earnings
    return answer
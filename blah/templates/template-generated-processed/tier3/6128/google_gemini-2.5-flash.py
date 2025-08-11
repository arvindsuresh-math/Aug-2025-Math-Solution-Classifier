from fractions import Fraction

def solve():
    """Index: 6128.
    Returns: the total earnings of the opera house from one show.
    """
    # L1
    num_rows = 150 # 150 rows
    seats_per_row = 10 # ten seats
    total_seats = num_rows * seats_per_row

    # L2
    percentage_not_taken = Fraction(20, 100) # 20% of the seats
    seats_not_taken = total_seats * percentage_not_taken

    # L3
    seats_taken = total_seats - seats_not_taken

    # L4
    ticket_cost = 10 # $10 per show
    total_earnings = ticket_cost * seats_taken

    # FA
    answer = total_earnings
    return answer
from fractions import Fraction

def solve():
    """Index: 4252.
    Returns: the price Maria paid for the ticket.
    """
    # L1
    discount_percentage = Fraction(40, 100) # 40% discount
    regular_price = 15 # regular price stands at $15
    discount_amount = discount_percentage * regular_price

    # L2
    ticket_price = regular_price - discount_amount

    # FA
    answer = ticket_price
    return answer
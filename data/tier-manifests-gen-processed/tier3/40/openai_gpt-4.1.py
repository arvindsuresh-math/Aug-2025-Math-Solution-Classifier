from fractions import Fraction

def solve():
    """Index: 40.
    Returns: the total amount Mr. Benson paid for all tickets.
    """
    # L1
    total_tickets = 12 # Mr. Benson bought 12 tickets
    discount_threshold = 10 # exceeds 10
    discounted_tickets = total_tickets - discount_threshold

    # L2
    ticket_price = 40 # concert ticket costs $40
    discount_percentage = Fraction(5, 100) # 5% discount
    discount_per_ticket = ticket_price * discount_percentage

    # L3
    discounted_ticket_price = ticket_price - discount_per_ticket

    # L4
    total_discounted = discounted_ticket_price * discounted_tickets

    # L5
    full_price_tickets = discount_threshold # the other ten tickets
    total_full_price = ticket_price * full_price_tickets

    # L6
    answer = total_full_price + total_discounted
    return answer
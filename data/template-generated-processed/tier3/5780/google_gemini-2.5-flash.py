from fractions import Fraction

def solve():
    """Index: 5780.
    Returns: the amount Travis needs to pay for his ticket.
    """
    # L1
    discount_percentage = Fraction(30, 100) # 30% discount
    regular_ticket_cost = 2000 # cost about $2000
    discount_amount = discount_percentage * regular_ticket_cost

    # L2
    final_cost = regular_ticket_cost - discount_amount

    # FA
    answer = final_cost
    return answer
from fractions import Fraction

def solve():
    """Index: 4778.
    Returns: the price Karsyn paid for the phone after negotiating.
    """
    # L1
    initial_price = 600 # phone's initial price was $600
    discount_percentage = Fraction(20, 100) # 20% of the initial price
    amount_paid_less = discount_percentage * initial_price

    # L2
    final_price = initial_price - amount_paid_less

    # FA
    answer = final_price
    return answer
from fractions import Fraction

def solve():
    """Index: 1398.
    Returns: the amount of money Charlotte should bring.
    """
    # L1
    discount_percentage = Fraction(20, 100) # discount of 20%
    original_price = 90 # original price is $90
    discount_amount = discount_percentage * original_price

    # L2
    money_to_bring = original_price - discount_amount

    # FA
    answer = money_to_bring
    return answer
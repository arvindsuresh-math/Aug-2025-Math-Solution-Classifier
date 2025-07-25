from fractions import Fraction

def solve():
    """Index: 2282.
    Returns: the amount of money Marcus saved by buying the shoes.
    """
    # L1
    original_price = 120 # a pair for $120
    discount_numerator = 30 # discount of 30%
    discount_denominator = 100 # discount of 30%
    discount_amount = original_price * Fraction(discount_numerator, discount_denominator)

    # L2
    price_after_discount = original_price - discount_amount

    # L3
    max_budget = 130 # not more than $130
    money_saved = max_budget - price_after_discount

    # FA
    answer = money_saved
    return answer
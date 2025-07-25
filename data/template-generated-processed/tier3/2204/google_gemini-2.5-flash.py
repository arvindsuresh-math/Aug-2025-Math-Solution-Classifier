from fractions import Fraction

def solve():
    """Index: 2204.
    Returns: the percent discount.
    """
    # L1
    original_price = 150 # cost $150 last week
    sale_price = 135 # now on sale for $135
    discount_amount = original_price - sale_price

    # L2
    discount_fraction = Fraction(discount_amount, original_price)

    # L3
    percentage_multiplier = 100 # WK
    percent_discount = discount_fraction * percentage_multiplier

    # FA
    answer = percent_discount
    return answer
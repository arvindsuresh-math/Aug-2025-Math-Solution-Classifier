from fractions import Fraction

def solve():
    """Index: 316.
    Returns: the new price of the bicycle after a 15% increase.
    """
    # L1
    last_year_price = 220 # had sold for $220 last year
    percent_increase = Fraction(15, 100) # increased by 15%
    increment = last_year_price * percent_increase

    # L2
    new_price = last_year_price + increment

    # FA
    answer = new_price
    return answer
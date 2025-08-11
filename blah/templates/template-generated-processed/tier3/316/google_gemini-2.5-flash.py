from fractions import Fraction

def solve():
    """Index: 316.
    Returns: the new selling price of the bicycle.
    """
    # L1
    original_price = 220 # $220 last year
    increase_percentage = Fraction(15, 100) # increased by 15%
    price_increase_amount = original_price * increase_percentage

    # L2
    new_price = original_price + price_increase_amount

    # FA
    answer = new_price
    return answer
from fractions import Fraction

def solve():
    """Index: 459.
    Returns: the total cost for Mr. Lucian to buy 4 lawnmowers at the current price.
    """
    # L1
    previous_price = 1800 # cost was $1800 a year ago
    price_increase_fraction = Fraction(2, 5) # 2/5 times less than the cost it goes for now
    price_increase = price_increase_fraction * previous_price

    # L2
    current_price = previous_price + price_increase

    # L3
    number_of_lawnmowers = 4 # buy 4 such lawnmowers
    total_cost = current_price * number_of_lawnmowers

    # FA
    answer = total_cost
    return answer
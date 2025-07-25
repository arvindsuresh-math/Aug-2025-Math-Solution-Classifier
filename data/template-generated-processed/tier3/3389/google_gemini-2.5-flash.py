from fractions import Fraction

def solve():
    """Index: 3389.
    Returns: the current price of RAM.
    """
    # L1
    increase_percentage = Fraction(30, 100) # increased by 30%
    initial_price = 50 # $50 before the fire
    price_increase_amount = increase_percentage * initial_price

    # L2
    price_before_stabilization = initial_price + price_increase_amount

    # L3
    decrease_percentage = Fraction(20, 100) # fell by 20%
    price_decrease_amount = decrease_percentage * price_before_stabilization

    # L4
    current_price = price_before_stabilization - price_decrease_amount

    # FA
    answer = current_price
    return answer
from fractions import Fraction

def solve():
    """Index: 4882.
    Returns: the number of shoppers who pay at the check-out lane.
    """
    # L1
    avoid_checkout_fraction = Fraction(5, 8) # 5/8 of shoppers at All Goods Available store prefer to avoid the check-out line
    total_shoppers = 480 # the number of shoppers in the store is 480
    shoppers_avoiding_checkout = avoid_checkout_fraction * total_shoppers

    # L2
    shoppers_preferring_checkout = total_shoppers - shoppers_avoiding_checkout

    # FA
    answer = shoppers_preferring_checkout
    return answer
from fractions import Fraction

def solve():
    """Index: 1178.
    Returns: the difference in pay between Oula and Tona.
    """
    # L1
    oula_deliveries = 96 # Oula made 96 deliveries
    pay_per_delivery = 100 # paid $100 for each delivery
    oula_earnings = oula_deliveries * pay_per_delivery

    # L2
    tona_delivery_fraction = Fraction(3, 4) # 3/4 times as many deliveries as Oula
    tona_deliveries = tona_delivery_fraction * oula_deliveries

    # L3
    tona_earnings = tona_deliveries * pay_per_delivery

    # L4
    pay_difference = oula_earnings - tona_earnings

    # FA
    answer = pay_difference
    return answer
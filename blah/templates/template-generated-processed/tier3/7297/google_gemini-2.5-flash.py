from fractions import Fraction

def solve():
    """Index: 7297.
    Returns: the total amount of money the two friends made on eBay.
    """
    # L1
    lauryn_earnings = 2000 # Lauryn made $2000 from selling the items on eBay
    aurelia_percentage = Fraction(70, 100) # 70% of what she sold on eBay
    aurelia_earnings = aurelia_percentage * lauryn_earnings

    # L2
    total_earnings = lauryn_earnings + aurelia_earnings

    # FA
    answer = total_earnings
    return answer
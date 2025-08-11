from fractions import Fraction

def solve():
    """Index: 6479.
    Returns: the total money Cheyenne made from selling the remaining items.
    """
    # L1
    cracked_fraction = Fraction(2, 5) # 2/5 of the pots cracked
    total_pots = 80 # made 80 clay pots
    cracked_pots = cracked_fraction * total_pots

    # L2
    sellable_pots = total_pots - cracked_pots

    # L3
    price_per_pot = 40 # $40 per clay pot
    total_earnings = price_per_pot * sellable_pots

    # FA
    answer = total_earnings
    return answer
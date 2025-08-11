from fractions import Fraction

def solve():
    """Index: 5705.
    Returns: the number of scarves Kiki will buy.
    """
    # L1
    hat_money_percentage = Fraction(60, 100) # 60% of her money on hats
    total_money = 90 # currently has $90
    money_on_hats = hat_money_percentage * total_money

    # L2
    money_on_scarves = total_money - money_on_hats

    # L3
    scarf_price = 2 # sold at $2 each
    num_scarves = money_on_scarves / scarf_price

    # FA
    answer = num_scarves
    return answer
from fractions import Fraction

def solve():
    """Index: 623.
    Returns: the number of cups of lemonade in the pitcher.
    """
    # L1
    iced_tea_per_drink = Fraction(1, 4) # 1/4 of a cup of iced tea
    lemonade_per_drink = Fraction(5, 4) # 1 and 1/4 of a cup of lemonade
    total_cups_per_drink = iced_tea_per_drink + lemonade_per_drink

    # L2
    total_pitcher_cups = 18 # 18 total cups of this drink
    num_drinks = total_pitcher_cups / float(total_cups_per_drink)

    # L3
    total_lemonade = num_drinks * float(lemonade_per_drink)

    # FA
    answer = total_lemonade
    return answer
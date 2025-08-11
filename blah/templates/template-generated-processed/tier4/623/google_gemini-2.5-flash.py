from fractions import Fraction

def solve():
    """Index: 623.
    Returns: the total cups of lemonade in the pitcher.
    """
    # L1
    iced_tea_per_drink = Fraction(1, 4) # 1/4 of a cup of iced tea
    lemonade_per_drink_whole = 1 # 1 and 1/4 of a cup of lemonade
    lemonade_per_drink_fraction = Fraction(1, 4) # 1 and 1/4 of a cup of lemonade
    total_cups_per_drink = iced_tea_per_drink + lemonade_per_drink_whole + lemonade_per_drink_fraction

    # L2
    total_cups_in_pitcher = 18 # 18 total cups of this drink
    total_drinks_in_pitcher = total_cups_in_pitcher / total_cups_per_drink

    # L3
    # lemonade_per_drink_whole and lemonade_per_drink_fraction are already defined from L1
    lemonade_amount_for_calc = lemonade_per_drink_whole + lemonade_per_drink_fraction
    total_lemonade_in_pitcher = total_drinks_in_pitcher * lemonade_amount_for_calc

    # FA
    answer = total_lemonade_in_pitcher
    return answer
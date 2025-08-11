from fractions import Fraction

def solve():
    """Index: 5920.
    Returns: the total amount Miley paid for all the cheese.
    """
    # L1
    swiss_packs = 5 # 5 packs of swiss cheese
    swiss_price_per_pack = 6 # $6 for swiss cheese
    cost_swiss_cheese = swiss_packs * swiss_price_per_pack

    # L2
    blue_cheese_grams = 600 # 600 grams of blue cheese
    grams_per_package = 200 # 200 grams of cheese in each package
    blue_cheese_packages = blue_cheese_grams / grams_per_package

    # L3
    blue_price_per_pack = 8 # $8 for blue cheese
    cost_blue_cheese = blue_cheese_packages * blue_price_per_pack

    # L4
    white_cheese_reduction_fraction = Fraction(1, 3) # one-third less white cheese
    white_cheese_reduction_grams = white_cheese_reduction_fraction * blue_cheese_grams

    # L5
    white_cheese_grams = blue_cheese_grams - white_cheese_reduction_grams

    # L6
    white_cheese_packages = white_cheese_grams / grams_per_package

    # L7
    white_price_per_pack = 5 # $5 for white cheese
    cost_white_cheese = white_cheese_packages * white_price_per_pack

    # L8
    total_cost = cost_swiss_cheese + cost_blue_cheese + cost_white_cheese

    # FA
    answer = total_cost
    return answer
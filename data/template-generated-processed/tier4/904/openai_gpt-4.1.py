from fractions import Fraction

def solve():
    """Index: 904.
    Returns: the number of key limes Audrey needs.
    """
    # L1
    recipe_cup = Fraction(1, 4) # 1/4 cup of key lime juice
    double_factor = 2 # she likes to double this amount
    total_cup = recipe_cup * double_factor

    # L2
    tablespoons_per_cup = 16 # 16 tablespoons in 1 cup
    total_cup_float = float(total_cup) # convert Fraction to float for multiplication
    total_tablespoons = tablespoons_per_cup * total_cup_float

    # L3
    tablespoon_per_lime = 1 # 1 key lime yields 1 tablespoon of juice
    key_limes_needed = tablespoon_per_lime * total_tablespoons

    # FA
    answer = key_limes_needed
    return answer
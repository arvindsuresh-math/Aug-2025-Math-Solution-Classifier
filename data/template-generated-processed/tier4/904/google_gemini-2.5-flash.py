from fractions import Fraction

def solve():
    """Index: 904.
    Returns: the number of key limes Audrey needs.
    """
    # L1
    initial_juice_fraction = Fraction(1, 4) # 1/4 cup of key lime juice
    doubled_juice_fraction_calc = initial_juice_fraction + initial_juice_fraction
    doubled_juice_amount_decimal = float(doubled_juice_fraction_calc)

    # L2
    tbs_per_cup = 16 # 16 tablespoons in 1 cup
    one_cup_value = 1 # WK
    total_tbs_juice = tbs_per_cup * doubled_juice_amount_decimal

    # L3
    tbs_per_key_lime = 1 # Each key lime yields 1 tablespoon of juice
    num_key_limes = tbs_per_key_lime * total_tbs_juice

    # FA
    answer = num_key_limes
    return answer
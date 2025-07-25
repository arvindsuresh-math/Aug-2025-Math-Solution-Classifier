def solve():
    """Index: 2383.
    Returns: the total combined money of Tom, Raquel, and Nataly.
    """
    # L1
    nataly_multiplier = 3 # Nataly has three times as much money as Raquel
    raquel_money = 40 # Raquel has $40
    nataly_money = nataly_multiplier * raquel_money

    # L2
    tom_fraction_numerator = 1 # a quarter as much money
    tom_fraction_denominator = 4 # a quarter as much money
    tom_money = tom_fraction_numerator / tom_fraction_denominator * nataly_money

    # L3
    combined_money = tom_money + nataly_money + raquel_money

    # FA
    answer = combined_money
    return answer
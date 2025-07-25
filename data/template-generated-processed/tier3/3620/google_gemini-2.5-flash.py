from fractions import Fraction

def solve():
    """Index: 3620.
    Returns: the total capacity of the tank.
    """
    # L1
    initial_fill_fraction = Fraction(1, 3) # tank is 1/3 full
    gallons_to_fill = 16 # 16 gallons of water are added
    full_tank_fraction = Fraction(1, 1) # WK
    empty_fraction = full_tank_fraction - initial_fill_fraction
    gallons_representing_empty_portion = gallons_to_fill

    # L2
    empty_fraction_value_text = Fraction(2, 3) # 2/3 of the tank
    one_third_fraction_value_text = Fraction(1, 3) # 1/3 of the tank
    divisor_for_one_third = 2 # WK
    gallons_representing_one_third = gallons_representing_empty_portion / divisor_for_one_third

    # L3
    total_capacity = gallons_to_fill + gallons_representing_one_third

    # FA
    answer = total_capacity
    return answer
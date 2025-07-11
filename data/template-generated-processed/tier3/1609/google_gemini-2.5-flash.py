from fractions import Fraction

def solve():
    """Index: 1609.
    Returns: the amount of water left in the bottle in liters.
    """
    # L1
    initial_water_volume = 4 # a 4-liter bottle full of water
    first_drink_fraction = Fraction(1, 4) # a quarter of the water
    first_drink_amount = first_drink_fraction * initial_water_volume

    # L2
    water_after_first_drink = initial_water_volume - first_drink_amount

    # L3
    second_drink_fraction = Fraction(2, 3) # 2/3rd of the remaining water
    second_drink_amount = second_drink_fraction * water_after_first_drink

    # L4
    water_remaining = water_after_first_drink - second_drink_amount

    # FA
    answer = water_remaining
    return answer
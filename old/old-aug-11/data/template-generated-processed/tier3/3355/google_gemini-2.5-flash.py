from fractions import Fraction

def solve():
    """Index: 3355.
    Returns: the final volume of water in the tank.
    """
    # L1
    initial_fill_fraction_numerator = 3 # 3/4 full
    initial_fill_fraction_denominator = 4 # 3/4 full
    tank_capacity = 8000 # capacity of 8000 gallons
    initial_water_volume = Fraction(initial_fill_fraction_numerator, initial_fill_fraction_denominator) * tank_capacity

    # L2
    empty_percentage_numerator = 40 # 40% of the total volume
    empty_percentage_denominator = 100 # 40% of the total volume
    emptied_volume = Fraction(empty_percentage_numerator, empty_percentage_denominator) * initial_water_volume

    # L3
    remaining_volume_after_empty = initial_water_volume - emptied_volume

    # L4
    fill_percentage_numerator = 30 # 30% of the volume of water remaining
    fill_percentage_denominator = 100 # 30% of the volume of water remaining
    filled_volume = Fraction(fill_percentage_numerator, fill_percentage_denominator) * remaining_volume_after_empty

    # L5
    final_water_volume = remaining_volume_after_empty + filled_volume

    # FA
    answer = final_water_volume
    return answer
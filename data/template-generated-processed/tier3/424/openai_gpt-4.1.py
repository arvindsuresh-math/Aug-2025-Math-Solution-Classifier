from fractions import Fraction

def solve():
    """Index: 424.
    Returns: the number of grams of rice Rose had left.
    """
    # L1
    initial_rice_kg = 10 # Rose had 10 kilograms of rice
    morning_fraction = Fraction(9, 10) # 9/10 kilograms in the morning
    morning_cooked_kg = initial_rice_kg * morning_fraction

    # L2
    rice_left_kg = initial_rice_kg - morning_cooked_kg

    # L3
    grams_per_kg = 1000 # WK
    rice_left_g = rice_left_kg * grams_per_kg

    # L4
    evening_fraction = Fraction(1, 4) # 1/4 of the remaining in the evening
    evening_cooked_g = rice_left_g * evening_fraction

    # L5
    rice_left_after_evening_g = rice_left_g - evening_cooked_g

    # FA
    answer = rice_left_after_evening_g
    return answer
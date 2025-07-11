from fractions import Fraction

def solve():
    """Index: 424.
    Returns: the total number of grams of rice Rose had left.
    """
    # L1
    initial_rice_kg = 10 # 10 kilograms of rice
    morning_fraction = Fraction(9, 10) # cooked 9/10 kilograms in the morning
    cooked_morning_kg = initial_rice_kg * morning_fraction

    # L2
    remaining_after_morning_kg = initial_rice_kg - cooked_morning_kg

    # L3
    grams_per_kilogram = 1000 # WK
    remaining_after_morning_grams = remaining_after_morning_kg * grams_per_kilogram

    # L4
    evening_fraction = Fraction(1, 4) # 1/4 of the remaining in the evening
    cooked_evening_grams = remaining_after_morning_grams * evening_fraction

    # L5
    final_remaining_grams = remaining_after_morning_grams - cooked_evening_grams

    # FA
    answer = final_remaining_grams
    return answer
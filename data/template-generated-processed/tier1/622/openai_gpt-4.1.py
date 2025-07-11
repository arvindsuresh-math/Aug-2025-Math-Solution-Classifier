def solve():
    """Index: 622.
    Returns: the total kilograms Anne is carrying when she carries both cats.
    """
    # L1
    female_cat_kg = 2 # Anne's female cat weighs 2 kilograms
    male_cat_multiplier = 2 # male cat is two times heavier
    male_cat_kg = female_cat_kg * male_cat_multiplier

    # L2
    total_kg = female_cat_kg + male_cat_kg

    # FA
    answer = total_kg
    return answer
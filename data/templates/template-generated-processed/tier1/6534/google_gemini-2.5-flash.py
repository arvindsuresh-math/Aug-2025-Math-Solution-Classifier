def solve():
    """Index: 6534.
    Returns: Ral's current age.
    """
    # L1
    suri_age_in_3_years = 16 # Suri's current age will be 16
    years_from_now = 3 # In 3 years
    suri_current_age = suri_age_in_3_years - years_from_now

    # L2
    multiplier_for_ral = 2 # Ral is twice as old as Suri
    ral_current_age = multiplier_for_ral * suri_current_age

    # FA
    answer = ral_current_age
    return answer
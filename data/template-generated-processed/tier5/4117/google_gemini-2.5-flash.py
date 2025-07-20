def solve():
    """Index: 4117.
    Returns: the number of years until Fouad's age is double Ahmed's age at that future time.
    """
    # L3
    ahmed_current_age = 11 # Ahmed is 11 years old
    fouad_current_age = 26 # Fouad is 26 years old
    multiplier_for_double = 2 # double # WK
    ahmed_age_term_expanded = ahmed_current_age * multiplier_for_double

    # L4
    years_to_double = fouad_current_age - ahmed_age_term_expanded

    # FA
    answer = years_to_double
    return answer
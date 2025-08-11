def solve():
    """Index: 1672.
    Returns: Ophelia's current age.
    """
    # L1
    years_ahead = 2 # In two years
    lennon_current_age = 8 # Lennon is currently eight years old
    lennon_age_in_two_years = years_ahead + lennon_current_age

    # L2
    ophelia_age_factor = 4 # four times as old
    ophelia_age_in_two_years = ophelia_age_factor * lennon_age_in_two_years

    # L3
    ophelia_current_age = ophelia_age_in_two_years - years_ahead

    # FA
    answer = ophelia_current_age
    return answer
from fractions import Fraction

def solve():
    """Index: 7381.
    Returns: Jessica's current age.
    """
    # L1
    mother_age_if_alive_now = 70 # she would have been 70
    years_later = 10 # ten years later
    mother_age_at_death = mother_age_if_alive_now - years_later

    # L2
    half_factor = Fraction(1, 2) # half her mother's age
    jessica_age_at_mother_death = half_factor * mother_age_at_death

    # L3
    jessica_current_age = years_later + jessica_age_at_mother_death

    # FA
    answer = jessica_current_age
    return answer
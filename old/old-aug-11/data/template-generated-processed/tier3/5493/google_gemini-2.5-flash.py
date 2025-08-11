from fractions import Fraction

def solve():
    """Index: 5493.
    Returns: Oscar's current age.
    """
    # L1
    future_age_fraction = Fraction(1, 2) # half of 80 years
    future_total_age = 80 # 80 years
    christina_future_age = future_age_fraction * future_total_age

    # L2
    years_to_come = 5 # in five years to come
    christina_current_age = christina_future_age - years_to_come

    # L3
    oscar_multiplier_fraction = Fraction(3, 5) # 3/5 times as old
    oscar_years_in_future = 15 # in 15 years
    oscar_age_in_15_years = oscar_multiplier_fraction * christina_current_age

    # L4
    oscar_current_age = oscar_age_in_15_years - oscar_years_in_future

    # FA
    answer = oscar_current_age
    return answer
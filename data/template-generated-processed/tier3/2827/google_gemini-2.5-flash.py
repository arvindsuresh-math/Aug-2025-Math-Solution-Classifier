from fractions import Fraction

def solve():
    """Index: 2827.
    Returns: the current age of the hospital.
    """
    # L1
    grant_current_age = 25 # Grant is currently 25 years old
    years_in_future = 5 # In five years
    grant_age_in_five_years = grant_current_age + years_in_future

    # L2
    grant_age_fraction = Fraction(2, 3) # 2/3 the age of the hospital
    whole_fraction = 1 # WK
    difference_fraction = whole_fraction - grant_age_fraction

    # L3
    hospital_age_fraction = Fraction(3, 3) # 3/3, which is the fraction representing the age of the hospital
    reciprocal_grant_age_fraction = Fraction(3, 2) # derived from 2/3
    hospital_age_in_five_years = hospital_age_fraction * grant_age_in_five_years * reciprocal_grant_age_fraction

    # L4
    hospital_current_age = hospital_age_in_five_years - years_in_future

    # FA
    answer = hospital_current_age
    return answer
from fractions import Fraction

def solve():
    """Index: 7472.
    Returns: the average age of Anika and Maddie in 15 years.
    """
    # L1
    anika_current_age = 30 # At 30, Anika
    years_in_future = 15 # in 15 years
    anika_age_in_15_years = anika_current_age + years_in_future

    # L2
    anika_maddie_ratio = Fraction(4, 3) # 4/3 the age of Maddie
    maddie_current_age = anika_maddie_ratio * anika_current_age

    # L3
    maddie_age_in_15_years = maddie_current_age + years_in_future

    # L4
    total_age_in_15_years = maddie_age_in_15_years + anika_age_in_15_years

    # L5
    number_of_people = 2 # WK
    average_age_in_15_years = total_age_in_15_years / number_of_people

    # FA
    answer = average_age_in_15_years
    return answer
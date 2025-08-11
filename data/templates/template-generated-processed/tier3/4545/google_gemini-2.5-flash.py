from fractions import Fraction

def solve():
    """Index: 4545.
    Returns: the total of their ages 10 years from now.
    """
    # L1
    jackson_current_age = 20 # Jackson is 20 years old now
    years_from_now = 10 # 10 years from now
    jackson_age_future = jackson_current_age + years_from_now

    # L2
    mandy_age_difference = 10 # Mandy is ten years older than Jackson
    mandy_current_age = jackson_current_age + mandy_age_difference

    # L3
    mandy_age_future = mandy_current_age + years_from_now

    # L4
    jackson_mandy_combined_future_age = jackson_age_future + mandy_age_future

    # L5
    adele_age_fraction = Fraction(3, 4) # Adele is 3/4 as old as Jackson
    adele_current_age = adele_age_fraction * jackson_current_age

    # L6
    adele_age_future = years_from_now + adele_current_age

    # L7
    total_future_age = adele_age_future + jackson_mandy_combined_future_age

    # FA
    answer = total_future_age
    return answer
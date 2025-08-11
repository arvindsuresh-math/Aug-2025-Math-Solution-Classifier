def solve():
    """Index: 149.
    Returns: Jayden's current age.
    """
    # L1
    ernesto_current_age = 11 # Ernesto is 11 years old
    years_in_future = 3 # In 3 years
    ernesto_age_in_future = ernesto_current_age + years_in_future

    # L2
    half_divisor = 2 # half of Ernesto's age
    jayden_age_in_future = ernesto_age_in_future / half_divisor

    # L3
    jayden_current_age = jayden_age_in_future - years_in_future

    # FA
    answer = jayden_current_age
    return answer
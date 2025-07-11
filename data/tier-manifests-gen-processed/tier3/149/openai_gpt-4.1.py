def solve():
    """Index: 149.
    Returns: Jayden's current age in years.
    """
    # L1
    ernesto_current_age = 11 # Ernesto is 11 years old
    years_in_future = 3 # In 3 years
    ernesto_future_age = ernesto_current_age + years_in_future

    # L2
    jayden_future_age = ernesto_future_age / 2

    # L3
    jayden_current_age = jayden_future_age - years_in_future

    # FA
    answer = jayden_current_age
    return answer
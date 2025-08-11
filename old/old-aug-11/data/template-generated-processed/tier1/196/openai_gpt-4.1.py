def solve():
    """Index: 196.
    Returns: Herbert's age next year.
    """
    # L1
    kris_age_now = 24 # Kris is 24 years old now
    herbert_younger_by = 10 # Herbert is 10 years younger than Kris
    herbert_age_now = kris_age_now - herbert_younger_by

    # L2
    one_year = 1 # next year
    herbert_age_next_year = herbert_age_now + one_year

    # FA
    answer = herbert_age_next_year
    return answer
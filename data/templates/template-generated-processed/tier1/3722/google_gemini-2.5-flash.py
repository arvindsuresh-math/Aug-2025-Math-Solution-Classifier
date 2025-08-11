def solve():
    """Index: 3722.
    Returns: Simon's age in 2010.
    """
    # L1
    jorge_age_2005 = 16 # In 2005, Jorge is 16 years old.
    age_difference = 24 # Jorge is 24 years younger than Simon.
    simon_age_2005 = jorge_age_2005 + age_difference

    # L2
    target_year = 2010 # In 2010, how old would Simon be?
    initial_year = 2005 # In 2005, Jorge is 16 years old.
    years_between = target_year - initial_year

    # L3
    simon_age_2010 = simon_age_2005 + years_between

    # FA
    answer = simon_age_2010
    return answer
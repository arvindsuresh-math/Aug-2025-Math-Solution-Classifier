def solve():
    """Index: 440.
    Returns: Cori's aunt's age today.
    """
    # L1
    cori_age_today = 3 # Cori is 3 years old today
    years_in_future = 5 # In 5 years
    cori_age_in_5_years = cori_age_today + years_in_future

    # L2
    aunt_age_multiple = 3 # one-third the age of her aunt
    aunt_age_in_5_years = cori_age_in_5_years * aunt_age_multiple

    # L3
    aunt_age_today = aunt_age_in_5_years - years_in_future

    # FA
    answer = aunt_age_today
    return answer
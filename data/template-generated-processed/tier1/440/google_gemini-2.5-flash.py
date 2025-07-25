def solve():
    """Index: 440.
    Returns: the current age of Cori's aunt.
    """
    # L1
    cori_current_age = 3 # Cori is 3 years old today
    years_in_future = 5 # In 5 years
    cori_future_age = cori_current_age + years_in_future

    # L2
    aunt_age_multiplier = 3 # one-third the age of her aunt
    aunt_future_age = cori_future_age * aunt_age_multiplier

    # L3
    aunt_current_age = aunt_future_age - years_in_future

    # FA
    answer = aunt_current_age
    return answer
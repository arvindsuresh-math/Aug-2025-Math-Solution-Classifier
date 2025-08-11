def solve():
    """Index: 3165.
    Returns: Talia's father's current age.
    """
    # L1
    talia_future_age = 20 # Talia will be 20 years old
    years_to_future = 7 # In seven years
    talia_current_age = talia_future_age - years_to_future

    # L2
    mom_age_multiplier = 3 # three times as old
    mom_current_age = mom_age_multiplier * talia_current_age

    # L3
    father_years_to_future = 3 # In three years
    father_current_age = mom_current_age - father_years_to_future

    # FA
    answer = father_current_age
    return answer
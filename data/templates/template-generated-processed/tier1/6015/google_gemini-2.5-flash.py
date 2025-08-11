def solve():
    """Index: 6015.
    Returns: Matt's current age.
    """
    # L1
    james_age_3_years_ago = 27 # 3 years ago James turned 27
    years_ago = 3 # 3 years ago
    james_current_age = james_age_3_years_ago + years_ago

    # L2
    years_in_future = 5 # In 5 years
    james_age_in_5_years = james_current_age + years_in_future

    # L3
    age_multiplier = 2 # twice James age
    matt_age_in_5_years = james_age_in_5_years * age_multiplier

    # L4
    matt_current_age = matt_age_in_5_years - years_in_future

    # FA
    answer = matt_current_age
    return answer
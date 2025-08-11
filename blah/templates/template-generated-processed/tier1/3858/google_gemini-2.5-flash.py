def solve():
    """Index: 3858.
    Returns: Bethany's current age.
    """
    # L1
    sister_age_in_5_years = 16 # her younger sister will be 16
    years_from_now = 5 # In 5 years
    sister_current_age = sister_age_in_5_years - years_from_now

    # L2
    years_ago = 3 # Three years ago
    sister_age_3_years_ago = sister_current_age - years_ago

    # L3
    age_multiplier = 2 # twice the age
    bethany_age_3_years_ago = sister_age_3_years_ago * age_multiplier

    # L4
    bethany_current_age = bethany_age_3_years_ago + years_ago

    # FA
    answer = bethany_current_age
    return answer
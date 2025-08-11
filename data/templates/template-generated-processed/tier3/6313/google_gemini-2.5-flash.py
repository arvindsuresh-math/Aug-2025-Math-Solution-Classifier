def solve():
    """Index: 6313.
    Returns: Trevor's age a decade ago.
    """
    # L1
    brother_current_age = 32 # his brother is now 32 years old
    years_ago = 20 # 20 years ago
    brother_age_20_years_ago = brother_current_age - years_ago

    # L2
    brother_age_multiplier = 2 # twice his age
    trevor_age_20_years_ago = brother_age_20_years_ago / brother_age_multiplier

    # L3
    trevor_current_age = trevor_age_20_years_ago + years_ago

    # L4
    decade_years = 10 # a decade ago
    trevor_age_decade_ago = trevor_current_age - decade_years

    # FA
    answer = trevor_age_decade_ago
    return answer
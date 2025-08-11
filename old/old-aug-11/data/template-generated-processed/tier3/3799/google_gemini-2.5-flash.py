def solve():
    """Index: 3799.
    Returns: Mary's current age.
    """
    # L1
    suzy_current_age = 20 # Suzy is 20 now
    years_later = 4 # In four years
    suzy_age_in_four_years = suzy_current_age + years_later

    # L2
    mary_age_multiplier = 2 # twice Mary's age then
    mary_age_in_four_years = suzy_age_in_four_years / mary_age_multiplier

    # L3
    mary_current_age = mary_age_in_four_years - years_later

    # FA
    answer = mary_current_age
    return answer
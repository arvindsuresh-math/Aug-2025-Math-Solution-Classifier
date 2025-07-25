def solve():
    """Index: 4502.
    Returns: the number of years until Arman's age is 40.
    """
    # L1
    years_ago = 4 # four years ago
    sister_age_years_ago = 2 # sister is 2 years old four years ago
    sister_current_age = years_ago + sister_age_years_ago

    # L2
    arman_age_multiplier = 6 # six times older than his sister
    arman_current_age = arman_age_multiplier * sister_current_age

    # L3
    arman_target_age = 40 # Arman's age be 40
    years_until_arman_40 = arman_target_age - arman_current_age

    # FA
    answer = years_until_arman_40
    return answer
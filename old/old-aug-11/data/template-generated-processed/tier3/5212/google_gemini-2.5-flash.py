def solve():
    """Index: 5212.
    Returns: Kody's current age.
    """
    # L1
    mohamed_multiplier = 2 # twice 30 years old
    mohamed_base_age = 30 # twice 30 years old
    mohamed_current_age = mohamed_multiplier * mohamed_base_age

    # L2
    years_ago = 4 # Four years ago
    mohamed_age_four_years_ago = mohamed_current_age - years_ago

    # L3
    kody_age_divisor = 2 # half as old
    kody_age_four_years_ago = mohamed_age_four_years_ago / kody_age_divisor

    # L4
    kody_current_age = kody_age_four_years_ago + years_ago

    # FA
    answer = kody_current_age
    return answer
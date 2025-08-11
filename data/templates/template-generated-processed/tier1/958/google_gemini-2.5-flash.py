def solve():
    """Index: 958.
    Returns: Djibo's sister's age today.
    """
    # L1
    djibo_current_age = 17 # Djibo is 17 years old
    years_ago = 5 # Five years ago
    djibo_age_five_years_ago = djibo_current_age - years_ago

    # L2
    sum_ages_five_years_ago = 35 # the sum was 35
    sister_age_five_years_ago = sum_ages_five_years_ago - djibo_age_five_years_ago

    # L3
    sister_current_age = sister_age_five_years_ago + years_ago

    # FA
    answer = sister_current_age
    return answer
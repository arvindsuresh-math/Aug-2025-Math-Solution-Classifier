def solve():
    """Index: 5692.
    Returns: the father's current age.
    """
    # L1
    sebastian_age_today = 40 # Sebastian is 40 years old
    age_difference = 10 # 10 years older than his sister
    sister_age_today = sebastian_age_today - age_difference

    # L2
    years_ago = 5 # Five years ago
    sebastian_age_five_years_ago = sebastian_age_today - years_ago

    # L3
    sister_age_five_years_ago = sister_age_today - years_ago

    # L4
    sum_ages_five_years_ago = sister_age_five_years_ago + sebastian_age_five_years_ago

    # L5
    father_age_fraction_numerator = 3 # 3/4 of their father's age
    father_age_fraction_denominator = 4 # 3/4 of their father's age
    father_age_five_years_ago = sum_ages_five_years_ago / (father_age_fraction_numerator / father_age_fraction_denominator)

    # L6
    father_age_today = father_age_five_years_ago + years_ago

    # FA
    answer = father_age_today
    return answer
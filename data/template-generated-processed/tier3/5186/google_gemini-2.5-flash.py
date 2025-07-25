def solve():
    """Index: 5186.
    Returns: Susan's age in 5 years.
    """
    # L1
    james_future_age = 37 # In 15 years James will turn 37
    years_to_future = 15 # In 15 years
    james_current_age = james_future_age - years_to_future

    # L2
    years_ago = 8 # 8 years ago
    james_age_8_years_ago = james_current_age - years_ago

    # L3
    age_ratio = 2 # twice Janet's age
    janet_age_8_years_ago = james_age_8_years_ago / age_ratio

    # L4
    janet_current_age = janet_age_8_years_ago + years_ago

    # L5
    janet_age_when_susan_born = 3 # Susan was born when Janet turned 3
    susan_current_age = janet_current_age - janet_age_when_susan_born

    # L6
    years_in_future = 5 # in 5 years
    susan_age_in_5_years = susan_current_age + years_in_future

    # FA
    answer = susan_age_in_5_years
    return answer
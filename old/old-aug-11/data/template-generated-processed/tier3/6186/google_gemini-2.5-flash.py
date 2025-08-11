def solve():
    """Index: 6186.
    Returns: Jim's age in 2 years.
    """
    # L1
    tom_age_five_years_ago = 32 # Tom turned 32 years old 5 years ago
    years_since_then = 5 # 5 years ago
    tom_current_age = tom_age_five_years_ago + years_since_then

    # L2
    years_ago_jim_was_older = 7 # 7 years ago Jim was 5 years older
    tom_age_seven_years_ago = tom_current_age - years_ago_jim_was_older

    # L3
    half_divisor = 2 # half Tom's age
    half_tom_age_seven_years_ago = tom_age_seven_years_ago / half_divisor

    # L4
    jim_older_than_half_tom_age = 5 # 5 years older than half Tom's age
    jim_age_seven_years_ago = half_tom_age_seven_years_ago + jim_older_than_half_tom_age

    # L5
    jim_current_age = jim_age_seven_years_ago + years_ago_jim_was_older

    # L6
    years_in_future = 2 # in 2 years
    jim_age_in_two_years = jim_current_age + years_in_future

    # FA
    answer = jim_age_in_two_years
    return answer
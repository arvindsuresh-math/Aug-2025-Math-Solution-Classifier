def solve():
    """Index: 1873.
    Returns: Sophia's age three years from now.
    """
    # L1
    jeremy_current_age = 40 # Jeremy's age is 40
    years_from_now = 3 # three years
    jeremy_age_in_three_years = jeremy_current_age + years_from_now

    # L2
    sebastian_age_difference = 4 # Sebastian is 4 years older than Jeremy
    sebastian_current_age = jeremy_current_age + sebastian_age_difference

    # L3
    sebastian_age_in_three_years = sebastian_current_age + years_from_now

    # L4
    jeremy_sebastian_total_age_in_three_years = sebastian_age_in_three_years + jeremy_age_in_three_years

    # L5
    total_age_all_three_in_three_years = 150 # The sum of the ages of Jeremy, Sebastian and Sophia in three years is 150
    sophia_age_in_three_years = total_age_all_three_in_three_years - jeremy_sebastian_total_age_in_three_years

    # FA
    answer = sophia_age_in_three_years
    return answer
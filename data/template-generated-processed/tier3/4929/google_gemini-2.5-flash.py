def solve():
    """Index: 4929.
    Returns: the age of James' older brother.
    """
    # L1
    john_current_age = 39 # John has just turned 39
    years_ago = 3 # 3 years ago
    john_age_3_years_ago = john_current_age - years_ago

    # L2
    age_multiplier = 2 # twice as old
    years_in_future_james = 6 # in 6 years
    james_age_in_6_years = john_age_3_years_ago / age_multiplier

    # L3
    james_current_age = james_age_in_6_years - years_in_future_james

    # L4
    brother_age_difference = 4 # 4 years older than James
    james_older_brother_age = james_current_age + brother_age_difference

    # FA
    answer = james_older_brother_age
    return answer
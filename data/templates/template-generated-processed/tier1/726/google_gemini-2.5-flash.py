def solve():
    """Index: 726.
    Returns: the sum of their present ages.
    """
    # L1
    jed_age_in_future = 25 # Jed will be 25 years old
    years_from_now = 10 # In 10 years
    jed_present_age = jed_age_in_future - years_from_now

    # L2
    jed_older_than_matt = 10 # Jed is 10 years older than Matt
    matt_present_age = jed_present_age - jed_older_than_matt

    # L3
    sum_of_present_ages = jed_present_age + matt_present_age

    # FA
    answer = sum_of_present_ages
    return answer
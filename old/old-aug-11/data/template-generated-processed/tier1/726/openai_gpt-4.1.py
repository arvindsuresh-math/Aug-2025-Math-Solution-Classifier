def solve():
    """Index: 726.
    Returns: the sum of Jed and Matt's present ages.
    """
    # L1
    jed_future_age = 25 # Jed will be 25 years old (in 10 years)
    years_in_future = 10 # in 10 years
    jed_present_age = jed_future_age - years_in_future

    # L2
    jed_older_than_matt = 10 # Jed is 10 years older than Matt
    matt_present_age = jed_present_age - jed_older_than_matt

    # L3
    sum_ages = jed_present_age + matt_present_age

    # FA
    answer = sum_ages
    return answer
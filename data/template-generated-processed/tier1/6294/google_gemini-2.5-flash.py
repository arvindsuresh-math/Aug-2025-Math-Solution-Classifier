def solve():
    """Index: 6294.
    Returns: Finley's current age.
    """
    # L1
    multiplier_twice = 2 # WK
    jill_age_now = 20 # Jill is 20 years old now
    twice_jill_age = multiplier_twice * jill_age_now

    # L2
    roger_more_than_twice_jill = 5 # 5 more than twice Jill's age
    roger_age_now = roger_more_than_twice_jill + twice_jill_age

    # L3
    years_in_future = 15 # In 15 years
    jill_age_future = jill_age_now + years_in_future

    # L4
    roger_age_future = roger_age_now + years_in_future

    # L5
    age_difference_future = roger_age_future - jill_age_future

    # L6
    finley_less_than_age_diff = 30 # 30 years less than Finley's age
    finley_age_future = finley_less_than_age_diff + age_difference_future

    # L7
    finley_age_now = finley_age_future - years_in_future

    # FA
    answer = finley_age_now
    return answer
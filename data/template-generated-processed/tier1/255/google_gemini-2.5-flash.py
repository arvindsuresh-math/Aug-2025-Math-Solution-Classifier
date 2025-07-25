def solve():
    """Index: 255.
    Returns: Matt's age 10 years from now.
    """
    # L1
    age_difference = 3 # younger than Matt by 3 years
    bush_current_age = 12 # Bush will be 12 years old
    matt_current_age = bush_current_age + age_difference

    # L2
    years_from_now = 10 # 10 years from now
    matt_future_age = years_from_now + matt_current_age

    # FA
    answer = matt_future_age
    return answer
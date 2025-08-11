def solve():
    """Index: 3127.
    Returns: the sum of the ages of Matt and Fem in two years.
    """
    # L1
    fem_current_age = 11 # Fem is 11 years old
    matt_age_multiplier = 4 # four times as old as Fem
    matt_current_age = fem_current_age * matt_age_multiplier

    # L2
    years_in_future = 2 # In two years
    matt_age_in_future = matt_current_age + years_in_future

    # L3
    fem_age_in_future = fem_current_age + years_in_future

    # L4
    sum_ages_in_future = matt_age_in_future + fem_age_in_future

    # FA
    answer = sum_ages_in_future
    return answer
def solve():
    """Index: 6717.
    Returns: Harriet's current age.
    """
    # L1
    mother_age = 60 # who is 60
    peter_age_fraction_denominator = 2 # half of his mother's age
    peter_current_age = mother_age / peter_age_fraction_denominator

    # L2
    years_in_future = 4 # In four years
    peter_age_in_four_years = peter_current_age + years_in_future

    # L3
    harriet_age_multiplier = 2 # twice as old as Harriet
    harriet_age_in_four_years = peter_age_in_four_years / harriet_age_multiplier

    # L4
    harriet_current_age = harriet_age_in_four_years - years_in_future

    # FA
    answer = harriet_current_age
    return answer
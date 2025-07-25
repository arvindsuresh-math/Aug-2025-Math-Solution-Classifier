def solve():
    """Index: 190.
    Returns: Dallas's current age.
    """
    # L1
    dexter_current_age = 8 # Dexter who is 8 right now
    darcy_age_factor = 2 # Darcy is twice as old as Dexter
    darcy_current_age = darcy_age_factor * dexter_current_age

    # L2
    years_passed = 1 # WK
    darcy_age_last_year = darcy_current_age - years_passed

    # L3
    dallas_age_factor = 3 # Dallas was 3 times the age of his sister Darcy
    dallas_age_last_year = dallas_age_factor * darcy_age_last_year

    # L4
    dallas_current_age = dallas_age_last_year + years_passed

    # FA
    answer = dallas_current_age
    return answer
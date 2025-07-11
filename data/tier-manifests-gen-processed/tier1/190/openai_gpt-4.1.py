def solve():
    """Index: 190.
    Returns: Dallas's current age.
    """
    # L1
    dexter_age = 8 # Dexter who is 8 right now
    darcy_multiplier = 2 # Darcy is twice as old as Dexter
    darcy_age = darcy_multiplier * dexter_age

    # L2
    last_year = 1 # last year
    darcy_last_year = darcy_age - last_year

    # L3
    dallas_multiplier = 3 # Dallas was 3 times the age of his sister Darcy
    dallas_last_year = dallas_multiplier * darcy_last_year

    # L4
    dallas_now = dallas_last_year + last_year

    # FA
    answer = dallas_now
    return answer
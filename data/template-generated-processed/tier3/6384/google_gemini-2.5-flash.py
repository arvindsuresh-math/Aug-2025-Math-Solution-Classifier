def solve():
    """Index: 6384.
    Returns: the total age of Sam, Sue, and Kendra in three years.
    """
    # L1
    kendra_current_age = 18 # Kendra is currently 18
    kendra_sam_multiplier = 3 # Kendra is 3 times as old as Sam
    sam_current_age = kendra_current_age / kendra_sam_multiplier

    # L2
    sam_sue_multiplier = 2 # Sam is twice as old as Sue
    sue_current_age = sam_current_age / sam_sue_multiplier

    # L3
    years_in_future = 3 # in 3 years
    sue_age_in_3_years = sue_current_age + years_in_future

    # L4
    sam_age_in_3_years = sam_current_age + years_in_future

    # L5
    kendra_age_in_3_years = kendra_current_age + years_in_future

    # L6
    total_age_in_3_years = sue_age_in_3_years + sam_age_in_3_years + kendra_age_in_3_years

    # FA
    answer = total_age_in_3_years
    return answer
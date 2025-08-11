def solve():
    """Index: 6786.
    Returns: Sandy's age when she achieves the world record.
    """
    # L1
    growth_rate_per_month = 0.1 # one-tenth of an inch per month
    months_per_year = 12 # WK
    growth_per_year = growth_rate_per_month * months_per_year

    # L2
    world_record_length = 26 # world record for longest fingernails is 26 inches
    current_length = 2 # Her fingernails are 2 inches long
    length_to_grow = world_record_length - current_length

    # L3
    years_to_grow = length_to_grow / growth_per_year

    # L4
    sandy_current_age = 12 # Sandy, who just turned 12 this month
    final_age = sandy_current_age + years_to_grow

    # FA
    answer = final_age
    return answer
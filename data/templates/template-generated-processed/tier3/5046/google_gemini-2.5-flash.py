def solve():
    """Index: 5046.
    Returns: the time in hours to fill the pool.
    """
    # L1
    num_hoses_type1 = 2 # Two of the hoses
    rate_hose_type1 = 2 # 2 gallons per minute
    combined_rate_type1_hoses = num_hoses_type1 * rate_hose_type1

    # L2
    num_hoses_type2 = 2 # The other two hoses
    rate_hose_type2 = 3 # 3 gallons per minute
    combined_rate_type2_hoses = num_hoses_type2 * rate_hose_type2

    # L3
    total_gallons_per_minute = combined_rate_type1_hoses + combined_rate_type2_hoses

    # L4
    pool_volume_gallons = 15000 # volume of 15,000 gallons
    time_to_fill_minutes = pool_volume_gallons / total_gallons_per_minute

    # L5
    minutes_per_hour = 60 # WK
    time_to_fill_hours = time_to_fill_minutes / minutes_per_hour

    # FA
    answer = time_to_fill_hours
    return answer
def solve():
    """Index: 1627.
    Returns: the total capacity of Grace's pool.
    """
    # L1
    hose_rate_1 = 50 # sprays 50 gallons/hour
    time_1 = 3 # waited for 3 hours
    gallons_first_period = hose_rate_1 * time_1

    # L2
    hose_rate_2 = 70 # add another hose that sprays 70 gallons/hour
    combined_rate = hose_rate_1 + hose_rate_2

    # L3
    time_2 = 2 # after 2 more hours
    gallons_second_period = combined_rate * time_2

    # L4
    total_capacity = gallons_second_period + gallons_first_period

    # FA
    answer = total_capacity
    return answer
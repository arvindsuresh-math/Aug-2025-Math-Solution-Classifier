def solve():
    """Index: 1627.
    Returns: the total water capacity of Grace's pool in gallons.
    """
    # L1
    hose1_rate = 50 # sprays 50 gallons/hour
    hours_first = 3 # waited for 3 hours
    gallons_first = hose1_rate * hours_first

    # L2
    hose2_rate = 70 # sprays 70 gallons/hour
    combined_rate = hose1_rate + hose2_rate

    # L3
    hours_second = 2 # after 2 more hours
    gallons_second = combined_rate * hours_second

    # L4
    total_capacity = gallons_second + gallons_first

    # FA
    answer = total_capacity
    return answer
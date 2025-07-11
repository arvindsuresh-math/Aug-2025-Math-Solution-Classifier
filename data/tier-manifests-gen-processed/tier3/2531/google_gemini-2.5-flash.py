def solve():
    """Index: 2531.
    Returns: the cost of the system per vent.
    """
    # L1
    num_zones = 2 # 2 conditioning zones
    vents_per_zone = 5 # each with 5 vents
    total_vents = num_zones * vents_per_zone

    # L2
    system_cost = 20000 # The cost of Joe's new HVAC system is $20,000
    cost_per_vent = system_cost / total_vents

    # FA
    answer = cost_per_vent
    return answer
def solve():
    """Index: 3009.
    Returns: the total number of vehicles that pass through the two bridges.
    """
    # L1
    vehicles_per_month_old_bridge = 2000 # 2000 vehicles passing through it every month
    months_per_year = 12 # WK
    total_vehicles_old_bridge_year = vehicles_per_month_old_bridge * months_per_year

    # L2
    percentage_numerator = 60 # increased by 60% more
    percentage_denominator = 100 # WK
    additional_vehicles_new_bridge_month = percentage_numerator / percentage_denominator * vehicles_per_month_old_bridge

    # L3
    total_vehicles_new_bridge_month = vehicles_per_month_old_bridge + additional_vehicles_new_bridge_month

    # L4
    total_vehicles_new_bridge_year = total_vehicles_new_bridge_month * months_per_year

    # L5
    total_vehicles_both_bridges_year = total_vehicles_new_bridge_year + total_vehicles_old_bridge_year

    # FA
    answer = total_vehicles_both_bridges_year
    return answer
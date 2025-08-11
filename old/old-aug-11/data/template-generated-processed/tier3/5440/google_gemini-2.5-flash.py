def solve():
    """Index: 5440.
    Returns: the number of weeks it will take Jaime to save the target amount.
    """
    # L1
    weekly_savings = 50 # Each week Jaime saves $50
    weeks_in_cycle = 2 # Every two weeks
    savings_per_two_weeks = weekly_savings * weeks_in_cycle

    # L2
    lunch_cost = 46 # spends $46 of her savings on a nice lunch
    net_savings_per_two_weeks = savings_per_two_weeks - lunch_cost

    # L3
    net_savings_per_week = net_savings_per_two_weeks / weeks_in_cycle

    # L4
    target_savings = 135 # save $135
    weeks_needed = target_savings / net_savings_per_week

    # FA
    answer = weeks_needed
    return answer
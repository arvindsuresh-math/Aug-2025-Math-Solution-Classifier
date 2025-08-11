def solve():
    """Index: 2612.
    Returns: the total cost of cat litter for 210 days.
    """
    # L1
    total_days = 210 # to last 210 days
    days_per_week = 7 # she changes out the litter weekly
    num_changes = total_days / days_per_week

    # L2
    litter_per_change = 15 # litter box holds 15 pounds of cat litter
    total_litter_pounds = num_changes * litter_per_change

    # L3
    container_size = 45 # 45-pound containers of cat litter
    num_containers = total_litter_pounds / container_size

    # L4
    cost_per_container = 21 # $21 each
    total_cost = num_containers * cost_per_container

    # FA
    answer = total_cost
    return answer
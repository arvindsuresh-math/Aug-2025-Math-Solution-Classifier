def solve():
    """Index: 4661.
    Returns: the total cost of the kitchen upgrade.
    """
    # L1
    num_cabinet_knobs = 18 # 18 cabinet knobs
    cost_per_cabinet_knob = 2.50 # $2.50 each
    total_cabinet_knob_cost = num_cabinet_knobs * cost_per_cabinet_knob

    # L2
    num_drawer_pulls = 8 # 8 drawer pulls
    cost_per_drawer_pull = 4.00 # $4.00
    total_drawer_pull_cost = num_drawer_pulls * cost_per_drawer_pull

    # L3
    total_upgrade_cost = total_cabinet_knob_cost + total_drawer_pull_cost

    # FA
    answer = total_upgrade_cost
    return answer
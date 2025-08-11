def solve():
    """Index: 5860.
    Returns: the amount of money Robe had saved before his car broke.
    """
    # L1
    repair_fee = 10 # used $10 from his savings to pay for the repair
    corner_light_multiplier = 2 # costs twice the price of the repair fee
    corner_light_cost = repair_fee * corner_light_multiplier

    # L2
    brake_disk_multiplier = 3 # each disk cost thrice the price of the corner light
    each_brake_disk_cost = corner_light_cost * brake_disk_multiplier

    # L3
    num_brake_disks = 2 # two brake disks
    total_brake_disks_cost = each_brake_disk_cost * num_brake_disks

    # L4
    total_spent = repair_fee + corner_light_cost + total_brake_disks_cost

    # L5
    savings_left = 480 # had $480 savings left
    initial_savings = savings_left + total_spent

    # FA
    answer = initial_savings
    return answer
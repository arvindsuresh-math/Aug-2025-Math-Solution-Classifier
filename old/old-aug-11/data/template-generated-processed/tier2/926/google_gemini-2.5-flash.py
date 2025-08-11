def solve():
    """Index: 926.
    Returns: the total amount Bailey will spend on towel sets.
    """
    # L1
    num_guest_sets = 2 # 2 new sets of towels
    cost_guest_set = 40.00 # $40.00 each
    cost_guest_towels = num_guest_sets * cost_guest_set

    # L2
    num_master_sets = 4 # 4 new sets
    cost_master_set = 50.00 # $50.00 each
    cost_master_towels = num_master_sets * cost_master_set

    # L3
    total_initial_cost = cost_guest_towels + cost_master_towels

    # L4
    discount_percent_decimal = 0.20 # 20% off
    discount_amount = total_initial_cost * discount_percent_decimal

    # L5
    final_cost = total_initial_cost - discount_amount

    # FA
    answer = final_cost
    return answer
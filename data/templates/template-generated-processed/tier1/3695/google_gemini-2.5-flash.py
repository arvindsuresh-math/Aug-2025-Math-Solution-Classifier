def solve():
    """Index: 3695.
    Returns: the amount of change Dusty receives.
    """
    # L1
    cost_single_slice = 4 # single layer cake slice is $4
    num_single_slices = 7 # buys 7 single layer cake slices
    cost_single_slices = cost_single_slice * num_single_slices

    # L2
    cost_double_slice = 7 # double layer cake slice is $7
    num_double_slices = 5 # 5 double layer cake slices
    cost_double_slices = cost_double_slice * num_double_slices

    # L3
    total_cost_cakes = cost_single_slices + cost_double_slices

    # L4
    bill_paid_with = 100 # pays with a $100 bill
    change_received = bill_paid_with - total_cost_cakes

    # FA
    answer = change_received
    return answer
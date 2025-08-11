def solve():
    """Index: 6223.
    Returns: the amount Bernie would save in three weeks.
    """
    # L1
    num_weeks = 3 # three weeks
    chocolates_per_week = 2 # two chocolates every week
    total_chocolates = num_weeks * chocolates_per_week

    # L2
    cost_local_store = 3 # One chocolate costs him $3
    total_cost_local = total_chocolates * cost_local_store

    # L3
    cost_different_store = 2 # each chocolate costs only $2
    total_cost_different = total_chocolates * cost_different_store

    # L4
    savings = total_cost_local - total_cost_different

    # FA
    answer = savings
    return answer
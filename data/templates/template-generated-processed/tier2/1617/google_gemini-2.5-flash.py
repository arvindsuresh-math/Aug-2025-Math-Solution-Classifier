def solve():
    """Index: 1617.
    Returns: the cost of a sandwich in cents.
    """
    # L1
    bread_slice_cost = 0.15 # a slice of bread costs $0.15
    num_bread_slices = 2 # two slices of bread
    cost_bread = bread_slice_cost * num_bread_slices

    # L2
    ham_slice_cost = 0.25 # a slice of ham costs $0.25
    cheese_slice_cost = 0.35 # a slice of cheese costs $0.35
    total_cost_dollars = cost_bread + ham_slice_cost + cheese_slice_cost

    # FA
    cents_per_dollar = 100 # WK
    answer = total_cost_dollars * cents_per_dollar
    return answer
def solve():
    """Index: 5661.
    Returns: the total amount of money raised from the fundraiser.
    """
    # L1
    pancake_cost_per_stack = 4.00 # $4.00
    num_pancake_stacks_sold = 60 # 60 stacks of pancakes
    total_pancake_revenue = pancake_cost_per_stack * num_pancake_stacks_sold

    # L2
    bacon_cost_per_slice = 2.00 # $2.00
    num_bacon_slices_sold = 90 # 90 slices of bacon
    total_bacon_revenue = bacon_cost_per_slice * num_bacon_slices_sold

    # L3
    total_revenue = total_pancake_revenue + total_bacon_revenue

    # FA
    answer = total_revenue
    return answer
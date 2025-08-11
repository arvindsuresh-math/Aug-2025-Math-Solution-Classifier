def solve():
    """Index: 6833.
    Returns: the total money the pie shop will make.
    """
    # L1
    cost_per_slice = 5 # $5 for a slice of pie
    slices_per_pie = 4 # cut each whole pie into 4 slices
    money_per_pie = cost_per_slice * slices_per_pie

    # L2
    num_pies_sold = 9 # sell 9 pies
    total_money_made = num_pies_sold * money_per_pie

    # FA
    answer = total_money_made
    return answer
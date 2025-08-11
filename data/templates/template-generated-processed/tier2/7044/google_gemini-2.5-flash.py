def solve():
    """Index: 7044.
    Returns: the total cost to sharpen Otto's knives.
    """
    # L1
    num_knives_group2 = 3 # for the next 3 knives
    cost_per_knife_group2 = 4.00 # $4.00 for the next 3 knives
    cost_group2 = num_knives_group2 * cost_per_knife_group2

    # L2
    num_knives_group3 = 5 # derived from 9 total - 1 first - 3 next from question
    cost_per_knife_group3 = 3.00 # $3.00 for any knife after that
    cost_group3 = num_knives_group3 * cost_per_knife_group3

    # L3
    cost_first_knife = 5.00 # $5.00 for the first knife
    total_cost = cost_first_knife + cost_group2 + cost_group3

    # FA
    answer = total_cost
    return answer
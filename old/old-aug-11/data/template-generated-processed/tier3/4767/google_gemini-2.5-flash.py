def solve():
    """Index: 4767.
    Returns: the cost of 2 pans.
    """
    # L1
    num_pots = 3 # 3 pots
    cost_per_pot = 20 # Each pot costs $20
    cost_of_pots = num_pots * cost_per_pot

    # L2
    total_cost_all_items = 100 # The total cost of Katerina's items is $100
    cost_of_4_pans = total_cost_all_items - cost_of_pots

    # L3
    num_pans_purchased = 4 # 4 pans
    cost_per_pan = cost_of_4_pans / num_pans_purchased

    # L4
    cost_of_2_pans = cost_per_pan + cost_per_pan

    # FA
    answer = cost_of_2_pans
    return answer
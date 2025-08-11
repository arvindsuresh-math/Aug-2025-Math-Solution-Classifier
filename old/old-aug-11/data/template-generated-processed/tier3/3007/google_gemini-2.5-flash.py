def solve():
    """Index: 3007.
    Returns: the cost of each skirt.
    """
    # L1
    total_spent = 50 # She spent a total of $50

    # L2
    art_supplies_cost = 20 # bought art supplies for $20
    num_skirts = 2 # 2 skirts

    # L3
    remaining_cost = total_spent - art_supplies_cost

    # L4
    cost_per_skirt = remaining_cost / num_skirts

    # L5
    # FA
    answer = cost_per_skirt
    return answer
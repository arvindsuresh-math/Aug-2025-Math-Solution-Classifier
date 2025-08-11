def solve():
    """Index: 2155.
    Returns: the cost of each bag.
    """
    # L1
    num_bags_to_sell = 100 # 100 bags
    price_per_bag = 10 # $10 per bag
    total_revenue = num_bags_to_sell * price_per_bag

    # L2
    desired_profit = 300 # make $300 in profit
    total_cost = total_revenue - desired_profit

    # L3
    cost_per_bag = total_cost / num_bags_to_sell

    # FA
    answer = cost_per_bag
    return answer
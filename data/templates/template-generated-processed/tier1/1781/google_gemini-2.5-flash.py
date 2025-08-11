def solve():
    """Index: 1781.
    Returns: the salesman's total profit.
    """
    # L1
    bags_sold_group1 = 17 # sold 17 of them
    price_group1 = 18 # for $18 at the swap meet
    revenue_group1 = bags_sold_group1 * price_group1

    # L2
    bags_sold_group2 = 10 # 10 were sold to a department store
    price_group2 = 25 # for $25 each
    revenue_group2 = bags_sold_group2 * price_group2

    # L3
    total_bags_sold_two_groups = bags_sold_group1 + bags_sold_group2

    # L4
    total_initial_bags = 48 # case of 48 backpacks
    price_group3 = 22 # remainder were sold for $22 each
    bags_sold_group3 = total_initial_bags - total_bags_sold_two_groups

    # L5
    revenue_group3 = bags_sold_group3 * price_group3

    # L6
    total_revenue = revenue_group1 + revenue_group2 + revenue_group3

    # L7
    initial_cost = 576 # bought a case of 48 backpacks for $576
    profit = total_revenue - initial_cost

    # FA
    answer = profit
    return answer
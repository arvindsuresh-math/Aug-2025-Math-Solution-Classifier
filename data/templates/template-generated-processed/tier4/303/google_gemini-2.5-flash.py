def solve():
    """Index: 303.
    Returns: the amount Tommy spends on flour.
    """
    # L1
    num_loaves = 12 # 12 loaves of bread
    flour_per_loaf = 4 # 4 pounds of flour per loaf
    total_flour_needed = num_loaves * flour_per_loaf

    # L2
    flour_bag_size_10lb = 10 # A 10-pound bag of flour
    num_bags_10lb_exact = total_flour_needed / flour_bag_size_10lb

    # L3
    lower_bound_10lb_bags = int(num_bags_10lb_exact)
    num_bags_10lb_actual = int(num_bags_10lb_exact) if num_bags_10lb_exact == int(num_bags_10lb_exact) else int(num_bags_10lb_exact) + 1

    # L4
    cost_10lb_bag = 10 # A 10-pound bag of flour costs $10
    cost_for_10lb_bags = num_bags_10lb_actual * cost_10lb_bag

    # L5
    flour_bag_size_12lb = 12 # a 12-pound bag
    num_bags_12lb_exact = total_flour_needed / flour_bag_size_12lb

    # L6
    cost_12lb_bag = 13 # a 12-pound bag costs $13
    cost_for_12lb_bags = num_bags_12lb_exact * cost_12lb_bag

    # L7
    cheapest_cost = min(cost_for_10lb_bags, cost_for_12lb_bags)

    # FA
    answer = cheapest_cost
    return answer
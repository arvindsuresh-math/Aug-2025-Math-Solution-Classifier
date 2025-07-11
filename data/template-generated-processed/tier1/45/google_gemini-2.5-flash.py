def solve():
    """Index: 45.
    Returns: the total cost of the unicorn piñata and the treats.
    """
    # L1
    cost_per_bag_reese = 9 # $9 per bag
    num_bags_reese = 4 # 4 bags of Reese's
    cost_reese = cost_per_bag_reese * num_bags_reese

    # L2
    cost_per_bag_snickers = 5 # $5 per bag
    num_bags_snickers = 3 # 3 bags of Snickers
    cost_snickers = cost_per_bag_snickers * num_bags_snickers

    # L3
    cost_per_bag_skittles = 7 # $7 per bag
    num_bags_skittles = 5 # 5 bags of Skittles
    cost_skittles = cost_per_bag_skittles * num_bags_skittles

    # L4
    unicorn_pinata_cost = 13 # unicorn piñata for $13
    total_cost = unicorn_pinata_cost + cost_reese + cost_snickers + cost_skittles

    # FA
    answer = total_cost
    return answer
def solve():
    """Index: 3136.
    Returns: the greatest number of balloons Mark can buy.
    """
    # L1
    total_money = 24 # He has $24
    small_bag_cost = 4 # small bags for $4
    num_small_bags = total_money / small_bag_cost

    # L2
    balloons_per_small_bag = 50 # the $4 bags contain 50 balloons
    total_balloons_small_bags = num_small_bags * balloons_per_small_bag

    # L3
    medium_bag_cost = 6 # medium bags for $6
    num_medium_bags = total_money / medium_bag_cost

    # L4
    balloons_per_medium_bag = 75 # the $6 bags contain 75 balloons
    total_balloons_medium_bags = num_medium_bags * balloons_per_medium_bag

    # L5
    extra_large_bag_cost = 12 # extra large bags for $12
    num_extra_large_bags = total_money / extra_large_bag_cost

    # L6
    balloons_per_extra_large_bag = 200 # the $12 bags contain 200 balloons
    total_balloons_extra_large_bags = num_extra_large_bags * balloons_per_extra_large_bag

    # L7
    max_balloons_possible = max(total_balloons_small_bags, total_balloons_medium_bags, total_balloons_extra_large_bags)

    # FA
    answer = max_balloons_possible
    return answer
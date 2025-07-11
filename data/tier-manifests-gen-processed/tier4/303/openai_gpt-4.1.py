def solve():
    """Index: 303.
    Returns: the minimum amount Tommy spends on flour to make 12 loaves of bread.
    """
    # L1
    num_loaves = 12 # Tommy is making 12 loaves of bread
    flour_per_loaf = 4 # 4 pounds of flour per loaf
    total_flour_needed = num_loaves * flour_per_loaf

    # L2
    ten_pound_bag_size = 10 # 10-pound bag of flour
    ten_bags_needed = total_flour_needed / ten_pound_bag_size

    # L3 (implicit, not a computation, just rounding up)
    ten_bags_to_buy = 5 # 4 < 4.8 < 5, so must buy 5 bags

    # L4
    ten_bag_price = 10 # $10 per 10-pound bag
    ten_bags_total_cost = ten_bags_to_buy * ten_bag_price

    # L5
    twelve_pound_bag_size = 12 # 12-pound bag of flour
    twelve_bags_needed = total_flour_needed / twelve_pound_bag_size

    # L6
    twelve_bags_to_buy = 4 # 48 / 12 = 4
    twelve_bag_price = 13 # $13 per 12-pound bag
    twelve_bags_total_cost = twelve_bags_to_buy * twelve_bag_price

    # L7
    answer = min(ten_bags_total_cost, twelve_bags_total_cost)
    return answer
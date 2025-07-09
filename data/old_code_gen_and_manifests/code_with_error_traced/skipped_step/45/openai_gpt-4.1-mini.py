def solve(
    pinata_cost: int = 13,  # unicorn piñata for $13
    num_bags_reeses: int = 4,  # 4 bags of Reese's
    cost_per_bag_reeses: int = 9,  # $9 per bag of Reese's
    num_bags_snickers: int = 3,  # 3 bags of Snickers
    cost_per_bag_snickers: int = 5,  # $5 per bag of Snickers
    num_bags_skittles: int = 5,  # 5 bags of Skittles
    cost_per_bag_skittles: int = 7  # $7 per bag of Skittles
):
    """Index: 45.
    Returns: the total cost of the unicorn piñata and all the treats.
    """

    #: L1
    total_cost_reeses = cost_per_bag_reeses * num_bags_reeses # eval: 36 = 9 * 4

    #: L2
    total_cost_snickers = cost_per_bag_snickers * num_bags_snickers # eval: 15 = 5 * 3

    #: L3

    #: L4
    total_cost = pinata_cost + total_cost_reeses + total_cost_snickers + cost_per_bag_reeses # eval: 73 = 13 + 36 + 15 + 9

    #: FA
    answer = total_cost
    return answer # eval: return 73

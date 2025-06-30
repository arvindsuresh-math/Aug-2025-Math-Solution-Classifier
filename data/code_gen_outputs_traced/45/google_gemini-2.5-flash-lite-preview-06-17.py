def solve(
    cost_pinata: int = 13, # a unicorn piñata for $13
    num_bags_reeses: int = 4, # 4 bags of Reese's
    cost_per_bag_reeses: int = 9, # for $9 per bag
    num_bags_snickers: int = 3, # 3 bags of Snickers
    cost_per_bag_snickers: int = 5, # for $5 per bag
    num_bags_skittles: int = 5, # 5 bags of Skittles
    cost_per_bag_skittles: int = 7 # for $7 per bag
):
    """Index: 45.
    Returns: the total cost of the piñata and all the treats.
    """

    #: L1
    cost_reeses = num_bags_reeses * cost_per_bag_reeses # eval: 36 = 4 * 9

    #: L2
    cost_snickers = num_bags_snickers * cost_per_bag_snickers # eval: 15 = 3 * 5

    #: L3
    cost_skittles = num_bags_skittles * cost_per_bag_skittles # eval: 35 = 5 * 7

    #: L4
    total_cost = cost_pinata + cost_reeses + cost_snickers + cost_skittles # eval: 99 = 13 + 36 + 15 + 35

    #: FA
    answer = total_cost # eval: 99 = 99
    return answer # eval: return 99

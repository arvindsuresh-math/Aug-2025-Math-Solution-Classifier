def solve(
    pinata_cost: int = 13, # bought a unicorn piñata for $13
    num_reese_bags: int = 4, # bought 4 bags of Reese's
    cost_per_reese_bag: int = 9, # for $9 per bag
    num_snickers_bags: int = 3, # 3 bags of Snickers
    cost_per_snickers_bag: int = 5, # for $5 per bag
    num_skittles_bags: int = 5, # and 5 bags of Skittles
    cost_per_skittles_bag: int = 7 # for $7 per bag
):
    """Index: 45.
    Returns: the total cost of the piñata and the treats.
    """

    #: L1
    cost_reese = num_reese_bags * cost_per_reese_bag # eval: 36 = 4 * 9

    #: L2
    cost_snickers = num_snickers_bags * cost_per_snickers_bag # eval: 15 = 3 * 5

    #: L3
    cost_skittles = num_skittles_bags * cost_per_skittles_bag # eval: 35 = 5 * 7

    #: L4
    total_cost = pinata_cost + cost_reese + num_snickers_bags + cost_skittles # eval: 87 = 13 + 36 + 3 + 35

    #: FA
    answer = total_cost
    return answer # eval: return 87

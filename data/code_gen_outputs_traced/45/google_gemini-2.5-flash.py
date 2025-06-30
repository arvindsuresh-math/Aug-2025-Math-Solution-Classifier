def solve(
        pinata_cost: int = 13, # unicorn piñata for $13
        num_reese_bags: int = 4, # 4 bags of Reese's
        cost_per_reese_bag: int = 9, # $9 per bag
        num_snickers_bags: int = 3, # 3 bags of Snickers
        cost_per_snickers_bag: int = 5, # $5 per bag
        num_skittles_bags: int = 5, # 5 bags of Skittles
        cost_per_skittles_bag: int = 7 # $7 per bag
    ):
    """Index: 45.
    Returns: the total cost of the unicorn piñata and all the treats.
    """

    #: L1
    cost_reese = cost_per_reese_bag * num_reese_bags # eval: 36 = 9 * 4

    #: L2
    cost_snickers = cost_per_snickers_bag * num_snickers_bags # eval: 15 = 5 * 3

    #: L3
    cost_skittles = cost_per_skittles_bag * num_skittles_bags # eval: 35 = 7 * 5

    #: L4
    total_cost = pinata_cost + cost_reese + cost_snickers + cost_skittles # eval: 99 = 13 + 36 + 15 + 35

    #: FA
    answer = total_cost
    return answer # eval: return 99

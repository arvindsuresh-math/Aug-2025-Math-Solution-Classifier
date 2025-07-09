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

    #: L2
    cost_snickers = cost_per_snickers_bag * num_snickers_bags

    #: L3
    cost_skittles = cost_per_skittles_bag * num_skittles_bags

    #: L4
    total_cost = pinata_cost + cost_per_reese_bag + cost_snickers + cost_skittles

    #: FA
    answer = total_cost
    return answer
def solve(
    cost_pinata: int = 13, # a unicorn piñata for $13
    num_reeses_bags: int = 4, # 4 bags of Reese's
    cost_reeses_bag: int = 9, # for $9 per bag
    num_snickers_bags: int = 3, # 3 bags of Snickers
    cost_snickers_bag: int = 5, # for $5 per bag
    num_skittles_bags: int = 5, # 5 bags of Skittles
    cost_skittles_bag: int = 7 # for $7 per bag
):
    """Index: 45.
    Returns: the total cost of the piñata and all the treats.
    """
    #: L1
    cost_reeses = cost_reeses_bag * num_reeses_bags

    #: L2
    cost_snickers = cost_snickers_bag * num_snickers_bags

    #: L3
    cost_skittles = cost_skittles_bag * num_skittles_bags

    #: L4
    total_cost = cost_pinata + cost_reeses + cost_snickers + cost_skittles

    answer = total_cost # FINAL ANSWER
    return answer
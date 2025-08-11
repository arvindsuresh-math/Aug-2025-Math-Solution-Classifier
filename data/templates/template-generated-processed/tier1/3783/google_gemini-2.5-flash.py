def solve():
    """Index: 3783.
    Returns: the total cost for doughnuts.
    """
    # L1
    num_chocolate_donuts = 10 # 10 kids want chocolate doughnuts
    cost_chocolate_per_donut = 2 # chocolate doughnuts cost $2 each
    cost_chocolate_donuts = num_chocolate_donuts * cost_chocolate_per_donut

    # L2
    num_glazed_donuts = 15 # 15 want glazed doughnuts
    cost_glazed_per_donut = 1 # glazed doughnuts cost $1 each
    cost_glazed_donuts = num_glazed_donuts * cost_glazed_per_donut

    # L3
    total_cost = cost_chocolate_donuts + cost_glazed_donuts

    # FA
    answer = total_cost
    return answer
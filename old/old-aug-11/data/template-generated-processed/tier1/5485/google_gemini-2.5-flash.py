def solve():
    """Index: 5485.
    Returns: the total money Mr. Zander paid for construction materials.
    """
    # L1
    bags_of_cement = 500 # 500 bags of cement
    price_per_bag_cement = 10 # $10 per bag
    cost_cement = bags_of_cement * price_per_bag_cement

    # L2
    num_lorries = 20 # twenty lorries of construction sand
    tons_per_lorry = 10 # each carrying 10 tons of sand
    total_tons_sand = num_lorries * tons_per_lorry

    # L3
    price_per_ton_sand = 40 # $40 per ton
    cost_sand = total_tons_sand * price_per_ton_sand

    # L4
    total_cost = cost_sand + cost_cement

    # FA
    answer = total_cost
    return answer
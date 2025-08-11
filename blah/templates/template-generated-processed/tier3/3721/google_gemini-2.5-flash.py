def solve():
    """Index: 3721.
    Returns: the cost of one chocolate bar.
    """
    # L1
    num_gummy_packs = 10 # 10 packs of gummy bears
    cost_per_gummy_pack = 2 # cost of a pack of gummy bears is $2
    total_gummy_cost = num_gummy_packs * cost_per_gummy_pack

    # L2
    cost_per_chocolate_chip_bag = 5 # a bag of chocolate chips costs $5
    num_chocolate_chip_bags = 20 # 20 bags of chocolate chips
    total_chocolate_chip_cost = cost_per_chocolate_chip_bag * num_chocolate_chip_bags

    # L3
    total_gummy_and_chip_cost = total_chocolate_chip_cost + total_gummy_cost

    # L4
    total_bill = 150 # Her total rang up to $150
    total_chocolate_bar_cost = total_bill - total_gummy_and_chip_cost

    # L5
    num_chocolate_bars = 10 # 10 chocolate bars
    cost_per_chocolate_bar = total_chocolate_bar_cost / num_chocolate_bars

    # FA
    answer = cost_per_chocolate_bar
    return answer
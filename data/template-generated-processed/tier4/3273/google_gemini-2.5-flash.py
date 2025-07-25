def solve():
    """Index: 3273.
    Returns: the number of ears of corn sold.
    """
    # L1
    cost_bag_seeds = 0.5 # It costs $.5 for a bag with 100 seeds
    seeds_per_bag = 100 # a bag with 100 seeds
    cost_per_seed = cost_bag_seeds / seeds_per_bag

    # L2
    seeds_per_ear = 4 # For every 4 seeds he plants, he gets one ear of corn
    cost_per_ear = cost_per_seed * seeds_per_ear

    # L3
    selling_price_per_ear = 0.1 # he can sell for $.1
    profit_per_ear = selling_price_per_ear - cost_per_ear

    # L4
    total_profit = 40 # If he makes $40 in profit
    ears_sold = total_profit / profit_per_ear

    # FA
    answer = ears_sold
    return answer
def solve():
    """Index: 3933.
    Returns: the net profit from the basil plants.
    """
    # L1
    seed_cost = 2.00 # spent $2.00 on a packet of basil seeds
    soil_cost = 8.00 # spent $8.00 on potting soil
    total_expenses = seed_cost + soil_cost

    # L2
    num_plants = 20 # yielded 20 basil plants
    price_per_plant = 5.00 # sells each basil plant for $5.00
    total_revenue = num_plants * price_per_plant

    # L3
    net_profit = total_revenue - total_expenses

    # FA
    answer = net_profit
    return answer
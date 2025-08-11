def solve():
    """Index: 832.
    Returns: the number of tanks John needs to buy.
    """
    # L1
    num_balloons = 1000 # John buys 1000 balloons
    liters_per_balloon = 10 # Each balloon holds 10 liters of air
    total_liters_needed = num_balloons * liters_per_balloon

    # L2
    tank_capacity = 500 # 500-liter tanks of gas
    num_tanks_needed = total_liters_needed / tank_capacity

    # FA
    answer = num_tanks_needed
    return answer
def solve():
    """Index: 1575.
    Returns: the profit Azalea made from her sheep farm.
    """
    # L1
    num_sheep = 200 # 200 sheep
    wool_per_sheep = 10 # produced 10 pounds of wool
    total_wool_pounds = num_sheep * wool_per_sheep

    # L2
    price_per_pound = 20 # sold a pound of wool at $20
    total_revenue = total_wool_pounds * price_per_pound

    # L3
    shearer_cost = 2000 # paid the shearer who had come to help her with the work $2000
    profit = total_revenue - shearer_cost

    # FA
    answer = profit
    return answer
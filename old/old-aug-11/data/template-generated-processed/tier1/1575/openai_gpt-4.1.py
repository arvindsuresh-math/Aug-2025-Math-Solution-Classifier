def solve():
    """Index: 1575.
    Returns: the profit Azalea made from the produce of her sheep farm.
    """
    # L1
    num_sheep = 200 # 200 sheep
    wool_per_sheep = 10 # Each of the sheared sheep produced 10 pounds of wool
    total_wool = num_sheep * wool_per_sheep

    # L2
    price_per_pound = 20 # sold a pound of wool at $20
    total_revenue = total_wool * price_per_pound

    # L3
    shearer_payment = 2000 # paid the shearer $2000
    profit = total_revenue - shearer_payment

    # FA
    answer = profit
    return answer
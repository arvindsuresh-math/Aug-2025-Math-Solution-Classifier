def solve():
    """Index: 4348.
    Returns: the total profit made.
    """
    # L1
    num_ducks = 30 # 30 ducks
    cost_per_duck = 10 # $10 each
    total_cost = num_ducks * cost_per_duck

    # L2
    weight_per_duck = 4 # weigh 4 pounds
    selling_price_per_pound = 5 # $5 per pound
    selling_price_per_duck = weight_per_duck * selling_price_per_pound

    # L3
    total_selling_price = num_ducks * selling_price_per_duck

    # L4
    profit = total_selling_price - total_cost

    # FA
    answer = profit
    return answer
def solve():
    """Index: 4096.
    Returns: the cost of the potatoes.
    """
    # L1
    num_chickens = 3 # 3 chickens
    price_per_chicken = 3 # $3 each
    cost_chickens = price_per_chicken * num_chickens

    # L2
    total_paid = 15 # $15 in total
    cost_potatoes = total_paid - cost_chickens

    # FA
    answer = cost_potatoes
    return answer
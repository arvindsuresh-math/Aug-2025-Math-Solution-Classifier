def solve():
    """Index: 3261.
    Returns: the price Benny has to charge for each pie.
    """
    # L1
    cost_per_pumpkin_pie = 3 # cost $3 each to make
    num_pumpkin_pies = 10 # ten pumpkin pies
    total_cost_pumpkin_pies = cost_per_pumpkin_pie * num_pumpkin_pies

    # L2
    cost_per_cherry_pie = 5 # cost $5 each to make
    num_cherry_pies = 12 # twelve cherry pies
    total_cost_cherry_pies = cost_per_cherry_pie * num_cherry_pies

    # L3
    desired_profit = 20 # profit of $20
    total_earnings_needed = total_cost_pumpkin_pies + total_cost_cherry_pies + desired_profit

    # L4
    total_pies_made = num_pumpkin_pies + num_cherry_pies
    price_per_pie = total_earnings_needed / total_pies_made

    # FA
    answer = price_per_pie
    return answer
def solve():
    """Index: 6879.
    Returns: the cost of each teddy bear.
    """
    # L1
    toy_price = 10 # $10 each
    num_initial_toys = 28 # 28 toys
    initial_toys_cost = toy_price * num_initial_toys

    # L2
    total_money_in_wallet = 580 # $580 in Louise’s wallet
    remaining_money = total_money_in_wallet - initial_toys_cost

    # L3
    num_teddy_bears = 20 # adds 20 teddy bears
    cost_per_teddy_bear = remaining_money / num_teddy_bears

    # FA
    answer = cost_per_teddy_bear
    return answer
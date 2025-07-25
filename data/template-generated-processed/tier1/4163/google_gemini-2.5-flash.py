def solve():
    """Index: 4163.
    Returns: the total profit made from stock transactions.
    """
    # L1
    cost_per_share_initial = 3 # costs $3 each
    initial_shares_bought = 20 # buys 20 shares
    initial_cost = cost_per_share_initial * initial_shares_bought

    # L2
    shares_sold_first_batch = 10 # sells 10 of those shares
    price_per_share_first_sale = 4 # for $4 each
    revenue_first_sale = shares_sold_first_batch * price_per_share_first_sale

    # L3
    remaining_shares = initial_shares_bought - shares_sold_first_batch

    # L4
    doubling_factor = 2 # doubling in value
    price_per_share_second_sale = cost_per_share_initial * doubling_factor

    # L5
    revenue_second_sale = remaining_shares * price_per_share_second_sale

    # L6
    total_revenue = revenue_second_sale + revenue_first_sale

    # L7
    profit = total_revenue - initial_cost

    # FA
    answer = profit
    return answer
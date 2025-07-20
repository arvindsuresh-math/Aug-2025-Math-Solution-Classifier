def solve():
    """Index: 7000.
    Returns: the total profit Jen makes in cents.
    """
    # L1
    buy_price_per_bar_cents = 80 # buys candy bars for 80 cents each
    num_bought_bars = 50 # buys 50 candy bars
    total_cost_cents = buy_price_per_bar_cents * num_bought_bars

    # L2
    cents_per_dollar = 100 # WK
    num_sold_bars = 48 # sells 48 of them
    total_revenue_cents = num_sold_bars * cents_per_dollar

    # L3
    total_profit_cents = total_revenue_cents - total_cost_cents

    # FA
    answer = total_profit_cents
    return answer
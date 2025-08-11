def solve():
    """Index: 3268.
    Returns: the total profit Romeo makes for all the chocolates he sells.
    """
    # L1
    total_selling_price = 90 # sells these chocolates for a total of $90
    num_bars = 5 # five bars of chocolate
    selling_price_per_bar = total_selling_price / num_bars

    # L2
    cost_per_bar = 5 # at $5 each
    packaging_cost_per_bar = 2 # packaging material that costs him $2 for each bar of chocolate
    profit_per_bar = selling_price_per_bar - cost_per_bar - packaging_cost_per_bar

    # L3
    total_profit = profit_per_bar * num_bars

    # FA
    answer = total_profit
    return answer
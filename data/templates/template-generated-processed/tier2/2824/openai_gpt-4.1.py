def solve():
    """Index: 2824.
    Returns: the total profit made by the taco truck if all beef is used.
    """
    # L1
    total_beef = 100 # buys 100 pounds of beef
    beef_per_taco = 0.25 # use .25 pounds of beef per taco
    num_tacos = total_beef / beef_per_taco

    # L2
    sale_price_per_taco = 2 # sell each taco for $2
    cost_per_taco = 1.5 # each taco takes $1.5 to make
    profit_per_taco = sale_price_per_taco - cost_per_taco

    # L3
    total_profit = num_tacos * profit_per_taco

    # FA
    answer = total_profit
    return answer
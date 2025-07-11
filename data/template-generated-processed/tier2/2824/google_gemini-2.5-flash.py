def solve():
    """Index: 2824.
    Returns: the total profit made by the taco truck.
    """
    # L1
    total_beef_pounds = 100 # 100 pounds of beef
    beef_per_taco = 0.25 # .25 pounds of beef per taco
    num_tacos = total_beef_pounds / beef_per_taco

    # L2
    taco_selling_price = 2 # sell each taco for $2
    taco_cost_to_make = 1.5 # each taco takes $1.5 to make
    profit_per_taco = taco_selling_price - taco_cost_to_make

    # L3
    total_profit = num_tacos * profit_per_taco

    # FA
    answer = total_profit
    return answer
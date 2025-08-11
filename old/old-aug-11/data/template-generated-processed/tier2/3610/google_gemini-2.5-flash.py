def solve():
    """Index: 3610.
    Returns: how much more Mary will spend than the rest of the firm put together.
    """
    # L1
    pasta_cost = 20 # a platter of pasta for $20
    bread_cost = 2 # a loaf of bread for $2
    mary_total_spend = pasta_cost + bread_cost

    # L2
    soda_cost_per_can = 1.5 # $1.50 each
    num_soda_cans = 4 # 4 cans of soda
    soda_total_cost = soda_cost_per_can * num_soda_cans

    # L3
    chicken_wings_cost = 10 # chicken wings for $10
    elle_andrea_total_spend = soda_total_cost + chicken_wings_cost

    # L4
    cake_cost = 5 # a cake that costs $5
    rest_of_firm_total_spend = elle_andrea_total_spend + cake_cost

    # L5
    mary_spend_difference = mary_total_spend - rest_of_firm_total_spend

    # FA
    answer = mary_spend_difference
    return answer
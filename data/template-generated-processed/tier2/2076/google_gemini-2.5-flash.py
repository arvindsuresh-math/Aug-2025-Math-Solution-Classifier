def solve():
    """Index: 2076.
    Returns: the cost of Sally McQueen.
    """
    # L1
    lightning_mcqueen_cost = 140000 # cost 140000$
    mater_cost_percent_decimal = 0.10 # 10 percent of that
    mater_cost = lightning_mcqueen_cost * mater_cost_percent_decimal

    # L2
    sally_cost_multiplier = 3 # triple what Mater costs
    sally_mcqueen_cost = mater_cost * sally_cost_multiplier

    # FA
    answer = sally_mcqueen_cost
    return answer
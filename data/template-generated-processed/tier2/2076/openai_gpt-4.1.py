def solve():
    """Index: 2076.
    Returns: the cost of Sally McQueen.
    """
    # L1
    mcqueen_cost = 140000 # Lightning McQueen, the race car, cost 140000$
    mater_percent = 0.10 # Mater only cost 10 percent of that
    mater_cost = mcqueen_cost * mater_percent

    # L2
    sally_multiplier = 3 # Sally McQueen cost triple what Mater costs
    sally_cost = mater_cost * sally_multiplier

    # FA
    answer = sally_cost
    return answer
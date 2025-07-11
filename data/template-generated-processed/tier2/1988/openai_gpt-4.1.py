def solve():
    """Index: 1988.
    Returns: how much more money Jackson has than Brandon now.
    """
    # L1
    initial_investment = 500 # both invest $500 in the stock market
    jackson_multiplier = 4 # Jackson's investment quadruples in value
    jackson_final = initial_investment * jackson_multiplier

    # L2
    brandon_percent_num = 20 # reduced to 20% of the initial value
    percent_factor = 0.01 # WK
    brandon_final = brandon_percent_num * percent_factor * initial_investment

    # L3
    difference = jackson_final - brandon_final

    # FA
    answer = difference
    return answer
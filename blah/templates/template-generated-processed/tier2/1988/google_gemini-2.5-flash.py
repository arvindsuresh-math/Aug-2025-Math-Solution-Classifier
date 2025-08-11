def solve():
    """Index: 1988.
    Returns: how much more money Jackson has than Brandon.
    """
    # L1
    initial_investment = 500 # invest $500
    jackson_multiplier = 4 # investment quadruples
    jackson_end_value = initial_investment * jackson_multiplier

    # L2
    brandon_percent_num = 20 # reduced to 20%
    percent_factor = 0.01 # WK
    brandon_end_value = brandon_percent_num * percent_factor * initial_investment

    # L3
    difference = jackson_end_value - brandon_end_value

    # FA
    answer = difference
    return answer
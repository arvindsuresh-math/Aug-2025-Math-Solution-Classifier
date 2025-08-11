def solve():
    """Index: 2146.
    Returns: the number of coconuts Dante had left after selling 10.
    """
    # L1
    paolo_coconuts = 14 # Paolo has 14 coconuts
    dante_multiplier = 3 # thrice as many coconuts as Paolo
    dante_coconuts = paolo_coconuts * dante_multiplier

    # L2
    dante_sold = 10 # Dante sold 10 of his coconuts
    dante_left = dante_coconuts - dante_sold

    # FA
    answer = dante_left
    return answer
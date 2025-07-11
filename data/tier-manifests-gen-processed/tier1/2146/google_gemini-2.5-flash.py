def solve():
    """Index: 2146.
    Returns: the number of coconuts Dante had left.
    """
    # L1
    paolo_coconuts = 14 # Paolo has 14 coconuts
    multiplier_thrice = 3 # thrice as many coconuts
    dante_initial_coconuts = paolo_coconuts * multiplier_thrice

    # L2
    dante_sold_coconuts = 10 # sold 10 of his coconuts
    dante_remaining_coconuts = dante_initial_coconuts - dante_sold_coconuts

    # FA
    answer = dante_remaining_coconuts
    return answer
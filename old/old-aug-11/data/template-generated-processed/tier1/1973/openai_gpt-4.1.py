def solve():
    """Index: 1973.
    Returns: the value of X, the amount Emily spent on Friday, in dollars.
    """
    # L4
    # X is unknown, but the sum is given
    total_spent = 120 # she spent $120 over the three days
    # L5
    sum_coeff = 6 # X + 2X + 3X = 6X
    # L6
    X = total_spent // sum_coeff
    # FA
    answer = X
    return answer
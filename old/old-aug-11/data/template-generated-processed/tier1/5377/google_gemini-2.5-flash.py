def solve():
    """Index: 5377.
    Returns: the amount Brianne will save in May.
    """
    # L1
    january_savings = 10 # $10 in January
    multiplier = 2 # twice as much
    february_savings = january_savings * multiplier

    # L2
    march_savings = february_savings * multiplier

    # L3
    april_savings = march_savings * multiplier

    # L4
    may_savings = april_savings * multiplier

    # FA
    answer = may_savings
    return answer
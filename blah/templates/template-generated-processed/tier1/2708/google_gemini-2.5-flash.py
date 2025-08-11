def solve():
    """Index: 2708.
    Returns: the amount Ofelia will save in May.
    """
    # L1
    initial_january_savings = 10 # In January, she saved $10
    multiplier_twice = 2 # twice the amount
    february_savings = initial_january_savings * multiplier_twice

    # L2
    march_savings = february_savings * multiplier_twice

    # L3
    april_savings = march_savings * multiplier_twice

    # L4
    may_savings = april_savings * multiplier_twice

    # FA
    answer = may_savings
    return answer
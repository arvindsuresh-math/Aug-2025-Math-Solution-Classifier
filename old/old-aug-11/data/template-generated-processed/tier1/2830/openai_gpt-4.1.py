def solve():
    """Index: 2830.
    Returns: the total amount Derek has saved by December.
    """
    # L1
    april_savings = 16 # $16 away in April
    multiplier = 2 # doubles his allowance savings each month
    may_savings = april_savings * multiplier

    # L2
    june_savings = may_savings * multiplier

    # L3
    july_savings = june_savings * multiplier

    # L4
    august_savings = july_savings * multiplier

    # L5
    september_savings = august_savings * multiplier

    # L6
    october_savings = september_savings * multiplier

    # L7
    november_savings = october_savings * multiplier

    # L8
    december_savings = november_savings * multiplier

    # FA
    answer = december_savings
    return answer
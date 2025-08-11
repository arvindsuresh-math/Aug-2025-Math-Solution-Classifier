def solve():
    """Index: 279.
    Returns: Robi's total savings after 6 months.
    """
    # L1
    jan_savings = 2 # $2 in January
    feb_savings = 4 # $4 in February
    mar_savings = 8 # $8 in March
    multiplier = 2 # WK
    april_savings = mar_savings * multiplier

    # L2
    may_savings = april_savings * multiplier

    # L3
    june_savings = may_savings * multiplier

    # L4
    total_savings = jan_savings + feb_savings + mar_savings + april_savings + may_savings + june_savings

    # FA
    answer = total_savings
    return answer
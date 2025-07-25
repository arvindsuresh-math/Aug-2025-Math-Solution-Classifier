def solve():
    """Index: 279.
    Returns: Robi's total savings after 6 months.
    """
    # L1
    march_savings = 8 # $8 in March
    april_savings = march_savings * 2

    # L2
    may_savings = april_savings * 2

    # L3
    june_savings = may_savings * 2

    # L4
    jan_savings = 2 # $2 in January
    feb_savings = 4 # $4 in February
    total_savings = jan_savings + feb_savings + march_savings + april_savings + may_savings + june_savings

    # FA
    answer = total_savings
    return answer
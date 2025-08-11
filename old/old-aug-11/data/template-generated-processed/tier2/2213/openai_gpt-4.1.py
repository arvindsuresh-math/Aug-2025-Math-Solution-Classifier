def solve():
    """Index: 2213.
    Returns: the amount Nancy will pay each year for her daughter's car insurance.
    """
    # L1
    nancy_percent = 0.4 # 40% of the cost
    monthly_cost = 80 # costs $80 a month
    nancy_monthly_payment = nancy_percent * monthly_cost

    # L2
    months_per_year = 12 # WK
    nancy_annual_payment = nancy_monthly_payment * months_per_year

    # FA
    answer = nancy_annual_payment
    return answer
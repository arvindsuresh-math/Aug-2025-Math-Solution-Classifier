def solve():
    """Index: 2213.
    Returns: how much Nancy will pay each year for car insurance.
    """
    # L1
    insurance_percentage_decimal = 0.4 # 40% of the cost
    monthly_total_cost = 80 # $80 a month
    nancys_monthly_portion = insurance_percentage_decimal * monthly_total_cost

    # L2
    months_per_year = 12 # WK
    nancys_annual_cost = nancys_monthly_portion * months_per_year

    # FA
    answer = nancys_annual_cost
    return answer
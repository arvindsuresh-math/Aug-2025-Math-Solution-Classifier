def solve():
    """Index: 2927.
    Returns: the additional dollars per month the company should make.
    """
    # L1
    monthly_sales = 4000 # sells $4000 worth of shoes every month
    months_per_year = 12 # WK
    current_annual_sales = months_per_year * monthly_sales

    # L2
    target_annual_sales = 60000 # make $60000 in an entire year
    additional_annual_sales_needed = target_annual_sales - current_annual_sales

    # L3
    additional_monthly_sales_needed = additional_annual_sales_needed / months_per_year

    # FA
    answer = additional_monthly_sales_needed
    return answer
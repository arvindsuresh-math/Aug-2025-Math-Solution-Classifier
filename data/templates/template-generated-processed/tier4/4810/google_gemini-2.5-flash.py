def solve():
    """Index: 4810.
    Returns: the amount Dawn saves each month.
    """
    # L1
    annual_salary = 48000 # 48,000 a year
    num_months_per_year = 12 # 12 equal monthly payments
    monthly_salary = annual_salary / num_months_per_year

    # L2
    monthly_savings_rate = 0.1 # saves 10% of her salary
    monthly_savings = monthly_salary * monthly_savings_rate

    # FA
    answer = monthly_savings
    return answer
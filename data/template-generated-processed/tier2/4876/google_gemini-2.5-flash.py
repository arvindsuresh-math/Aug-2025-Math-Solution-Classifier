def solve():
    """Index: 4876.
    Returns: MegaCorp's fine in dollars.
    """
    # L1
    mining_daily_profit = 3000000 # $3,000,000 from mining
    oil_daily_profit = 5000000 # $5,000,000 from oil refining
    total_daily_profit = mining_daily_profit + oil_daily_profit

    # L2
    days_per_year = 365 # WK
    annual_earnings = days_per_year * total_daily_profit

    # L3
    monthly_expenses = 30000000 # monthly expenses are $30,000,000
    months_per_year = 12 # WK
    annual_expenses = monthly_expenses * months_per_year

    # L4
    annual_profit = annual_earnings - annual_expenses

    # L5
    fine_percent_num = 1 # fined 1%
    percent_to_decimal_factor = 0.01 # WK
    fine_amount = annual_profit * fine_percent_num * percent_to_decimal_factor

    # FA
    answer = fine_amount
    return answer
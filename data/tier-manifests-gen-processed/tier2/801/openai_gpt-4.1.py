def solve():
    """Index: 801.
    Returns: the amount of money Alex has left after taxes, water bill, and tithe.
    """
    # L1
    weekly_income = 500 # $500 a week
    tax_percent_num = 10 # 10% of his weekly income is deducted as tax
    percent_factor = 0.01 # WK
    income_tax = weekly_income * tax_percent_num * percent_factor

    # L2
    tithe_percent_num = 10 # gives away another 10% of his weekly income as a tithe
    tithe = weekly_income * tithe_percent_num * percent_factor

    # L3
    water_bill = 55 # weekly water bill for $55
    total_expenses = income_tax + water_bill + tithe

    # L4
    answer = weekly_income - total_expenses
    return answer
def solve():
    """Index: 6732.
    Returns: the amount of child support the ex owes Nancy.
    """
    # L1
    first_period_years = 3 # For 3 years
    initial_annual_income = 30000 # made $30,000/year
    income_first_period = first_period_years * initial_annual_income

    # L2
    raise_percent = 20 # got a 20% raise
    percent_to_decimal_factor = 0.01 # WK
    raise_amount = initial_annual_income * raise_percent * percent_to_decimal_factor

    # L3
    new_annual_income = raise_amount + initial_annual_income

    # L4
    second_period_years = 4 # for the next four years
    income_second_period = second_period_years * new_annual_income

    # L5
    total_earnings = income_second_period + income_first_period

    # L6
    child_support_percent = 30 # pay 30% of his income
    total_supposed_to_pay = total_earnings * child_support_percent * percent_to_decimal_factor

    # L7
    amount_paid = 1200 # only ever paid $1,200
    amount_owed = total_supposed_to_pay - amount_paid

    # FA
    answer = amount_owed
    return answer
def solve():
    """Index: 4056.
    Returns: the difference between their weekly incomes.
    """
    # L1
    terry_daily_income = 24 # Terry's daily income is $24
    days_per_week = 7 # Working 7 days a week
    terry_weekly_income = terry_daily_income * days_per_week

    # L2
    jordan_daily_income = 30 # Jordan's daily income is $30
    jordan_weekly_income = jordan_daily_income * days_per_week

    # L3
    income_difference = jordan_weekly_income - terry_weekly_income

    # FA
    answer = income_difference
    return answer
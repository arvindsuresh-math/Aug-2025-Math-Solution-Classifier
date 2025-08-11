def solve():
    """Index: 6188.
    Returns: the amount of money Dino has left at the end of the month.
    """
    # L1
    hours_job1 = 20 # works 20 hours a month
    rate_job1 = 10 # making $10 an hour
    income_job1 = hours_job1 * rate_job1

    # L2
    hours_job2 = 30 # works 30 hours a month
    rate_job2 = 20 # making $20 an hour
    income_job2 = hours_job2 * rate_job2

    # L3
    hours_job3 = 5 # works 5 hours a month
    rate_job3 = 40 # making $40 an hour
    income_job3 = hours_job3 * rate_job3

    # L4
    total_income = income_job1 + income_job3 + income_job2

    # L5
    monthly_expenses = 500 # pays $500 a month in expenses
    money_left = total_income - monthly_expenses

    # FA
    answer = money_left
    return answer
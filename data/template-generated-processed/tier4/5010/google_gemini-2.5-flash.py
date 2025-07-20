def solve():
    """Index: 5010.
    Returns: the amount of money Jackson needs to set aside per paycheck.
    """
    # L1
    total_savings_goal = 3000.00 # save $3,000.00
    months_to_save = 15 # 15 months away
    monthly_savings_needed = total_savings_goal / months_to_save

    # L2
    paychecks_per_month = 2 # 2 times a month
    savings_per_paycheck = monthly_savings_needed / paychecks_per_month

    # FA
    answer = savings_per_paycheck
    return answer
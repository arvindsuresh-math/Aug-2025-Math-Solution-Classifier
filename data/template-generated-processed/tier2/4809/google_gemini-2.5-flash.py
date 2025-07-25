def solve():
    """Index: 4809.
    Returns: the interest charged by the loan shark in the second month.
    """
    # L1
    initial_loan_amount = 200 # $200
    interest_rate_percent = 10 # 10% interest
    percent_factor = 0.01 # WK
    first_month_interest = initial_loan_amount * interest_rate_percent * percent_factor

    # L2
    new_loan_total = initial_loan_amount + first_month_interest

    # L3
    second_month_interest = new_loan_total * interest_rate_percent * percent_factor

    # FA
    answer = second_month_interest
    return answer
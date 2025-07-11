def solve():
    """Index: 199.
    Returns: the additional amount Gary is spending per month.
    """
    # L1
    repayment_years_short = 2 # pay him back the full amount in 2 years
    months_per_year = 12 # WK
    months_short_term = repayment_years_short * months_per_year

    # L2
    loan_amount = 6000 # Gary bought his first used car for $6,000
    monthly_payment_short_term = loan_amount / months_short_term

    # L3
    repayment_years_long = 5 # pay him back the full amount over 5 years
    months_long_term = repayment_years_long * months_per_year

    # L4
    monthly_payment_long_term = loan_amount / months_long_term

    # L5
    additional_monthly_payment = monthly_payment_short_term - monthly_payment_long_term

    # FA
    answer = additional_monthly_payment
    return answer
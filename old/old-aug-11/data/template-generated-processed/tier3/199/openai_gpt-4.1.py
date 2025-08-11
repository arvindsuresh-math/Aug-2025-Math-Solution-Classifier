def solve():
    """Index: 199.
    Returns: the additional amount Gary spends per month to pay off the loan in 2 years instead of 5.
    """
    # L1
    years_2 = 2 # 2 years
    months_per_year = 12 # WK
    months_2_years = years_2 * months_per_year

    # L2
    loan_amount = 6000 # $6,000
    monthly_payment_2_years = loan_amount / months_2_years

    # L3
    years_5 = 5 # 5 years
    months_5_years = years_5 * months_per_year

    # L4
    monthly_payment_5_years = loan_amount / months_5_years

    # L5
    # FA
    answer = monthly_payment_2_years - monthly_payment_5_years
    return answer
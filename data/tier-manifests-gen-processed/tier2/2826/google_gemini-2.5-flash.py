def solve():
    """Index: 2826.
    Returns: the total amount of the loan including the down payment.
    """
    # L1
    loan_term_years = 5 # 5 years
    months_per_year = 12 # WK
    total_months = loan_term_years * months_per_year

    # L2
    monthly_payment = 600.00 # monthly payments are $600.00
    total_payments_amount = monthly_payment * total_months

    # L3
    down_payment = 10000 # $10,000 down as a down payment
    total_loan_amount = down_payment + total_payments_amount

    # FA
    answer = total_loan_amount
    return answer
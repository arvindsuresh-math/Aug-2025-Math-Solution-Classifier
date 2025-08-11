def solve():
    """Index: 2826.
    Returns: the total loan amount including the down payment.
    """
    # L1
    years = 5 # pay entire amount back in 5 years
    months_per_year = 12 # WK
    total_months = years * months_per_year

    # L2
    monthly_payment = 600.00 # monthly payments are $600.00
    total_payments = monthly_payment * total_months

    # L3
    down_payment = 10000 # $10,000 down as a down payment
    loan_amount = down_payment + total_payments

    # FA
    answer = loan_amount
    return answer
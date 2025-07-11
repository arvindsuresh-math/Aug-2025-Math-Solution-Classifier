def solve():
    """Index: 1079.
    Returns: the amount Mr. Roberts can save by paying cash for the television.
    """
    # L1
    monthly_payment = 30 # $30 a month
    num_months = 12 # 12 months
    total_monthly_payments = monthly_payment * num_months

    # L2
    down_payment = 120 # $120 down payment
    total_non_cash_cost = total_monthly_payments + down_payment

    # L3
    cash_price = 400 # $400 cash
    savings = total_non_cash_cost - cash_price

    # FA
    answer = savings
    return answer
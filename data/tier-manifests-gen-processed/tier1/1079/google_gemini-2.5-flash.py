def solve():
    """Index: 1079.
    Returns: the amount saved by paying cash.
    """
    # L1
    monthly_payment = 30 # $30 a month
    num_months = 12 # for 12 months
    total_monthly_payment = monthly_payment * num_months

    # L2
    down_payment = 120 # $120 down payment
    total_cost_installment = total_monthly_payment + down_payment

    # L3
    cash_price = 400 # $400 cash
    savings = total_cost_installment - cash_price

    # FA
    answer = savings
    return answer
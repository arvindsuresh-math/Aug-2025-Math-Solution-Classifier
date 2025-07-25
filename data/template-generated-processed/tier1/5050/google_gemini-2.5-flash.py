def solve():
    """Index: 5050.
    Returns: the amount Loisa will save if she buys the tablet in cash instead of on installment.
    """
    # L1
    payment_first_period = 40 # $40 for the first 4 months
    months_first_period = 4 # first 4 months
    total_first_period_payment = payment_first_period * months_first_period

    # L2
    payment_second_period = 35 # $35 for the next four months
    months_second_period = 4 # next four months
    total_second_period_payment = payment_second_period * months_second_period

    # L3
    payment_third_period = 30 # $30 for the last four months
    months_third_period = 4 # last four months
    total_third_period_payment = payment_third_period * months_third_period

    # L4
    down_payment = 100 # $100 as a down payment
    total_months_installment = 12 # installment plan for 12 months
    total_installment_cost = down_payment + total_first_period_payment + total_second_period_payment + total_third_period_payment

    # L5
    cash_price = 450 # tablet that costs $450 cash
    savings = total_installment_cost - cash_price

    # FA
    answer = savings
    return answer
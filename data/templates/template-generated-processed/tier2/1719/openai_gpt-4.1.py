def solve():
    """Index: 1719.
    Returns: the new balance on Tonya's credit card after payment and interest.
    """
    # L1
    initial_balance = 150.00 # $150.00 on her credit card
    payment = 50.00 # $50.00 payment
    balance_after_payment = initial_balance - payment

    # L2
    interest_rate_decimal = 0.20 # .20*100
    interest_rate_percent = 20 # 20% interest
    interest = interest_rate_decimal * balance_after_payment

    # L3
    new_balance = balance_after_payment + interest

    # FA
    answer = new_balance
    return answer
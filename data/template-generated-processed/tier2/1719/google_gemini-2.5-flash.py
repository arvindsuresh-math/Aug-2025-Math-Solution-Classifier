def solve():
    """Index: 1719.
    Returns: the new balance on the credit card.
    """
    # L1
    initial_balance = 150.00 # Tonya has $150.00 on her credit card.
    payment_amount = 50.00 # she makes a $50.00 payment
    balance_after_payment = initial_balance - payment_amount

    # L2
    interest_rate_percent = 20 # charged 20% interest
    interest_rate_decimal = 0.20 # from solution text: .20*100
    interest_amount = interest_rate_decimal * balance_after_payment

    # L3
    final_balance = balance_after_payment + interest_amount

    # FA
    answer = final_balance
    return answer
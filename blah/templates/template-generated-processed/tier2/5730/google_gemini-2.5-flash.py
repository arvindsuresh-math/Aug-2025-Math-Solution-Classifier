def solve():
    """Index: 5730.
    Returns: the current balance on his credit card.
    """
    # L1
    initial_balance = 50.00 # $50.00 balance
    interest_rate_percent = 20 # 20% interest fee
    interest_rate_decimal = 0.20 # 20% interest fee
    first_interest_fee = initial_balance * interest_rate_decimal

    # L2
    balance_after_first_interest = initial_balance + first_interest_fee

    # L3
    new_charge = 20.00 # puts $20.00 on his credit card
    balance_after_new_charge = balance_after_first_interest + new_charge

    # L4
    second_interest_fee = balance_after_new_charge * interest_rate_decimal

    # L5
    final_balance = balance_after_new_charge + second_interest_fee

    # FA
    answer = final_balance
    return answer
def solve():
    """Index: 6490.
    Returns: Lucy's final bank balance.
    """
    # L1
    initial_balance = 65 # Lucy has $65 in the bank
    deposit_amount = 15 # made a $15 deposit
    balance_after_deposit = initial_balance + deposit_amount

    # L2
    withdrawal_amount = 4 # a $4 withdrawal
    final_balance = balance_after_deposit - withdrawal_amount

    # FA
    answer = final_balance
    return answer
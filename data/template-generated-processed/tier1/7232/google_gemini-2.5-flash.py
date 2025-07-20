def solve():
    """Index: 7232.
    Returns: the total amount of money in Emma's bank account.
    """
    # L1
    initial_balance = 230 # saved $230 in her bank account
    withdrawal_amount = 60 # withdrew $60
    balance_after_withdrawal = initial_balance - withdrawal_amount

    # L2
    deposit_multiplier = 2 # deposited twice as much money as she withdrew
    deposit_amount = withdrawal_amount * deposit_multiplier

    # L3
    final_balance = balance_after_withdrawal + deposit_amount

    # FA
    answer = final_balance
    return answer
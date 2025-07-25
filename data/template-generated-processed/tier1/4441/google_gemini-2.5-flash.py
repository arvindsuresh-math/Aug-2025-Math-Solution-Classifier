def solve():
    """Index: 4441.
    Returns: the amount Wilson withdrew last month.
    """
    # L1
    initial_balance = 150 # $150 in his bank account
    deposited_last_month = 17 # deposited $17
    balance_before_withdrawal = initial_balance + deposited_last_month

    # L2
    more_than_two_months_ago = 16 # $16 more than what is in his account two months ago
    current_balance = initial_balance + more_than_two_months_ago

    # L3
    deposited_this_month = 21 # deposited $21 this month
    balance_after_withdrawal_last_month = current_balance - deposited_this_month

    # L4
    amount_withdrawn = balance_before_withdrawal - balance_after_withdrawal_last_month

    # FA
    answer = amount_withdrawn
    return answer
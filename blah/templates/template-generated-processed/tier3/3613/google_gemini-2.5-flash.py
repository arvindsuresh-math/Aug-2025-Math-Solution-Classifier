def solve():
    """Index: 3613.
    Returns: the initial balance in Pam's bank account.
    """
    # L1
    current_balance = 950 # current balance is $950
    amount_withdrawn = 250 # withdrew $250
    balance_before_withdrawal = current_balance + amount_withdrawn

    # L2
    triple_factor = 3 # tripled during the year
    initial_balance = balance_before_withdrawal / triple_factor

    # FA
    answer = initial_balance
    return answer
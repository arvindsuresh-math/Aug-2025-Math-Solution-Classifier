def solve():
    """Index: 702.
    Returns: the amount of money left in Lily's account.
    """
    # L1
    initial_account_balance = 55 # Lily had $55 in her account
    cost_shirt = 7 # She spent $7 on a shirt
    balance_after_shirt = initial_account_balance - cost_shirt

    # L2
    multiplier_thrice = 3 # spent thrice as much
    cost_another_shop = cost_shirt * multiplier_thrice

    # L3
    final_balance = balance_after_shirt - cost_another_shop

    # FA
    answer = final_balance
    return answer
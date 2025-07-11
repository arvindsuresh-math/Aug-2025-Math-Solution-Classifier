def solve():
    """Index: 281.
    Returns: the combined balance of both Gina's accounts.
    """
    # L1
    betty_balance = 3456 # Betty's account balance is $3,456
    quarter_divisor = 4 # a quarter of the balance
    gina_single_account_balance = betty_balance / quarter_divisor

    # L2
    combined_gina_balance = gina_single_account_balance + gina_single_account_balance

    # FA
    answer = combined_gina_balance
    return answer
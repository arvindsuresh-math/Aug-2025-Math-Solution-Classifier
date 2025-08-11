def solve():
    """Index: 4614.
    Returns: the amount of dollars in the account before the check was deposited.
    """
    # L1
    check_value = 50 # $50 birthday check
    fraction_denominator = 4 # a quarter of her new balance
    new_balance = check_value * fraction_denominator

    # L2
    balance_before_check = new_balance - check_value

    # FA
    answer = balance_before_check
    return answer
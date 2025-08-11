def solve():
    """Index: 6574.
    Returns: the total amount Jack will pay back.
    """
    # L1
    interest_rate_decimal = 0.1 # interest of 10%
    loan_amount = 1200 # borrowed $1200
    interest_amount = interest_rate_decimal * loan_amount

    # L2
    total_payback_amount = loan_amount + interest_amount

    # FA
    answer = total_payback_amount
    return answer
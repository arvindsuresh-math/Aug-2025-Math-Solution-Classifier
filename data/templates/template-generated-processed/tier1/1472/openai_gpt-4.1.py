def solve():
    """Index: 1472.
    Returns: the amount Shara will still owe her brother 4 months from now.
    """
    # L1
    months_so_far = 6 # 6 months ago
    monthly_payment = 10 # $10 per month
    amount_returned = monthly_payment * months_so_far

    # L2
    # She currently owes the same as what she has already returned (half left)
    current_debt = amount_returned

    # L3
    months_future = 4 # 4 months from now
    future_payment = monthly_payment * months_future

    # L4
    remaining_debt = current_debt - future_payment

    # FA
    answer = remaining_debt
    return answer
def solve():
    """Index: 1472.
    Returns: the amount Shara will still owe her brother.
    """
    # L1
    amount_per_month = 10 # returned $10 per month
    months_returned = 6 # 6 months ago
    total_returned_so_far = amount_per_month * months_returned

    # L2
    amount_currently_owed = total_returned_so_far

    # L3
    months_from_now = 4 # 4 months from now
    additional_payment = amount_per_month * months_from_now

    # L4
    remaining_debt = amount_currently_owed - additional_payment

    # FA
    answer = remaining_debt
    return answer
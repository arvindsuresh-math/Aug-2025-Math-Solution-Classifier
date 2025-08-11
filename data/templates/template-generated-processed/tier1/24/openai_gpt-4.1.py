def solve():
    """Index: 24.
    Returns: the amount of credit Mary needs to pay before her next shopping trip.
    """
    # L1
    paid_tuesday = 15 # paid $15 of it on Tuesday
    paid_thursday = 23 # paid $23 of it on Thursday
    total_paid = paid_tuesday + paid_thursday

    # L2
    credit_limit = 100 # allowed a credit of $100
    remaining_credit = credit_limit - total_paid

    # FA
    answer = remaining_credit
    return answer
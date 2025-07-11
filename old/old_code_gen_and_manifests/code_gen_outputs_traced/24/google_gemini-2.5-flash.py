def solve(
        credit_limit: int = 100, # a credit of $100
        payment_tuesday: int = 15, # paid $15 of it on Tuesday
        payment_thursday: int = 23 # paid $23 of it on Thursday
    ):
    """Index: 24.
    Returns: the amount of credit Mary still needs to pay before her next shopping trip.
    """

    #: L1
    total_paid_so_far = payment_tuesday + payment_thursday # eval: 38 = 15 + 23

    #: L2
    remaining_credit_to_pay = credit_limit - total_paid_so_far # eval: 62 = 100 - 38

    #: FA
    answer = remaining_credit_to_pay
    return answer # eval: return 62

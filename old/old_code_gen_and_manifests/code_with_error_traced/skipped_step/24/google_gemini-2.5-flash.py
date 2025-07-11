def solve(
        credit_limit: int = 100, # a credit of $100
        payment_tuesday: int = 15, # paid $15 of it on Tuesday
        payment_thursday: int = 23 # paid $23 of it on Thursday
    ):
    """Index: 24.
    Returns: the amount of credit Mary still needs to pay before her next shopping trip.
    """

    #: L1

    #: L2
    remaining_credit_to_pay = credit_limit - payment_tuesday # eval: 85 = 100 - 15

    #: FA
    answer = remaining_credit_to_pay
    return answer # eval: return 85

def solve(
    credit_limit: int = 100, # Mary is allowed a credit of $100
    payment_tuesday: int = 15, # paid $15 of it on Tuesday
    payment_thursday: int = 23 # and $23 of it on Thursday
):
    """Index: 24.
    Returns: the amount of credit Mary still needs to pay before her next shopping trip.
    """

    #: L1
    total_paid = payment_tuesday - payment_thursday # eval: -8 = 15 - 23

    #: L2
    remaining_credit = credit_limit - total_paid # eval: 108 = 100 - -8

    #: FA
    answer = remaining_credit
    return answer # eval: return 108

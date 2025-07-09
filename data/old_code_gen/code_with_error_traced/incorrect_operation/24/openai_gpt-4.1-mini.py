def solve(
    credit_limit: int = 100,  # credit of $100
    payment_tuesday: int = 15,  # paid $15 on Tuesday
    payment_thursday: int = 23  # paid $23 on Thursday
):
    """Index: 24.
    Returns: the remaining credit Mary needs to pay before her next shopping trip.
    """

    #: L1
    total_paid = payment_tuesday - payment_thursday # eval: -8 = 15 - 23

    #: L2
    remaining_credit = credit_limit - total_paid # eval: 108 = 100 - -8

    #: FA
    answer = remaining_credit
    return answer # eval: return 108

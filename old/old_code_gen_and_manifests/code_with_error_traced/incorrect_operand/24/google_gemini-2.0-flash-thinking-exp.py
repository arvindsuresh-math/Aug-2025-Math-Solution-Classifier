def solve(
    credit_limit: int = 100, # allowed a credit of $100
    paid_on_tuesday: int = 15, # paid $15 of it on Tuesday
    paid_on_thursday: int = 23 # paid $23 of it on Thursday
):
    """Index: 24.
    Returns: the amount of credit Mary still needs to pay.
    """

    #: L1
    total_paid = paid_on_tuesday + credit_limit # eval: 115 = 15 + 100

    #: L2
    remaining_credit = credit_limit - total_paid # eval: -15 = 100 - 115

    #: FA
    answer = remaining_credit
    return answer # eval: return -15

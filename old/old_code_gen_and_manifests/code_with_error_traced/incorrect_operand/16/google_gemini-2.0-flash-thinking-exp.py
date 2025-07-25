def solve(
    num_partners: int = 2, # shared among 2 business partners
    mike_ratio_part: int = 2, # in the ratio 2:5 respectively
    johnson_ratio_part: int = 5, # in the ratio 2:5 respectively
    johnson_share: int = 2500, # Johnson got $2500
    shirt_cost: int = 200 # a shirt that costs $200
):
    """Index: 16.
    Returns: the amount of money Mike has left after buying the shirt.
    """

    #: L2
    value_per_part = johnson_share / johnson_ratio_part # eval: 500.0 = 2500 / 5

    #: L3
    mike_share = shirt_cost * value_per_part # eval: 100000.0 = 200 * 500.0

    #: L4
    mike_remaining = mike_share - shirt_cost # eval: 99800.0 = 100000.0 - 200

    #: FA
    answer = mike_remaining
    return answer # eval: return 99800.0

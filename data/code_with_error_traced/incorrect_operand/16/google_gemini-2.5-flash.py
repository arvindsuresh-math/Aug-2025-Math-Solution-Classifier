def solve(
        num_partners: int = 2, # 2 business partners
        mike_ratio_part: int = 2, # in the ratio 2:5 respectively
        johnson_ratio_part: int = 5, # in the ratio 2:5 respectively
        johnson_share: int = 2500, # If Johnson got $2500
        shirt_cost: int = 200 # on a shirt that costs $200
    ):
    """Index: 16.
    Returns: Mike's remaining share after spending on a shirt.
    """

    #: L2
    value_per_part = johnson_share / num_partners # eval: 1250.0 = 2500 / 2

    #: L3
    mike_share = mike_ratio_part * value_per_part # eval: 2500.0 = 2 * 1250.0

    #: L4
    mike_remaining_share = mike_share - shirt_cost # eval: 2300.0 = 2500.0 - 200

    #: FA
    answer = mike_remaining_share
    return answer # eval: return 2300.0

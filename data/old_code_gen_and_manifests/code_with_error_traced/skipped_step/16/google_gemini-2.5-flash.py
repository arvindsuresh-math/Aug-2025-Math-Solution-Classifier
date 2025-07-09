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
    value_per_part = johnson_share / johnson_ratio_part # eval: 500.0 = 2500 / 5

    #: L3
    mike_share = mike_ratio_part * value_per_part # eval: 1000.0 = 2 * 500.0

    #: L4

    #: FA
    answer = num_partners
    return answer # eval: return 2

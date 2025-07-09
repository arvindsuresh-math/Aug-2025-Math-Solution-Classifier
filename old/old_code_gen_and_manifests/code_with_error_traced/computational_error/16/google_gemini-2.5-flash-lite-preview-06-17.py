def solve(
    johnson_share: int = 2500, # If Johnson got $2500
    ratio_mike: int = 2, # Mike and Johnson in the ratio 2:5 respectively
    ratio_johnson: int = 5, # Mike and Johnson in the ratio 2:5 respectively
    shirt_cost: int = 200 # a shirt that costs $200
):
    """Index: 16.
    Returns: the amount of money Mike will have left after buying a shirt.
    """

    #: L2
    value_per_part = johnson_share / ratio_johnson # eval: 500.0 = 2500 / 5

    #: L3
    mike_share = 999.0 # eval: 999.0 = 999.0

    #: L4
    mike_remaining_share = mike_share - shirt_cost # eval: 799.0 = 999.0 - 200

    #: FA
    answer = mike_remaining_share
    return answer # eval: return 799.0

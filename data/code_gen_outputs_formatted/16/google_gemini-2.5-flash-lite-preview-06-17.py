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
    value_per_part = johnson_share / ratio_johnson

    #: L3
    mike_share = ratio_mike * value_per_part

    #: L4
    mike_remaining_share = mike_share - shirt_cost

    answer = mike_remaining_share # FINAL ANSWER
    return answer
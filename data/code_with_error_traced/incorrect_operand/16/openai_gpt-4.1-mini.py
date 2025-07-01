def solve(
    johnson_share: int = 2500,  # Johnson got $2500
    shirt_cost: int = 200  # shirt costs $200
):
    """Index: 16.
    Returns: the amount Mike has left after buying the shirt.
    """

    #: L2
    value_per_part = shirt_cost / 5 # eval: 40.0 = 200 / 5

    #: L3
    mike_share = 2 * value_per_part # eval: 80.0 = 2 * 40.0

    #: L4
    mike_after_shirt = mike_share - shirt_cost # eval: -120.0 = 80.0 - 200

    #: FA
    answer = mike_after_shirt
    return answer # eval: return -120.0

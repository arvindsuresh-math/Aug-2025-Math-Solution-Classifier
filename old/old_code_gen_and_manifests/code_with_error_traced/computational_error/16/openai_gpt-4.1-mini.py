def solve(
    johnson_share: int = 2500,  # Johnson got $2500
    shirt_cost: int = 200  # shirt costs $200
):
    """Index: 16.
    Returns: the amount Mike has left after buying the shirt.
    """

    #: L2
    value_per_part = 490.0 # eval: 490.0 = 490.0

    #: L3
    mike_share = 2 * value_per_part # eval: 980.0 = 2 * 490.0

    #: L4
    mike_after_shirt = mike_share - shirt_cost # eval: 780.0 = 980.0 - 200

    #: FA
    answer = mike_after_shirt
    return answer # eval: return 780.0

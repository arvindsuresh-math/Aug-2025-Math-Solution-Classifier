def solve(
    johnson_share: int = 2500,  # Johnson got $2500
    shirt_cost: int = 200  # shirt costs $200
):
    """Index: 16.
    Returns: the amount Mike has left after buying the shirt.
    """
    #: L2
    value_per_part = johnson_share / 5 # eval: 500.0 = 2500 / 5
    #: L3
    mike_share = 2 * value_per_part # eval: 1000.0 = 2 * 500.0
    #: L4
    mike_after_shirt = mike_share - shirt_cost # eval: 800.0 = 1000.0 - 200
    answer = mike_after_shirt  # FINAL ANSWER # eval: 800.0 = 800.0  # FINAL ANSWER
    return answer # eval: return 800.0
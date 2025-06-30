def solve(
    johnson_share_ratio: int = 5,  # Johnson gets 5 parts
    mike_share_ratio: int = 2,  # Mike gets 2 parts
    johnson_amount: int = 2500,  # Johnson got $2500
    shirt_cost: int = 200  # shirt costs $200
):
    """Index: 16.
    Returns: the amount of money Mike has left after buying a shirt."""

    #: L2
    part_value = johnson_amount / johnson_share_ratio # eval: 500.0 = 2500 / 5

    #: L3
    mike_total_share = mike_share_ratio * part_value # eval: 1000.0 = 2 * 500.0

    #: L4
    mike_remaining_amount = mike_total_share - shirt_cost # eval: 800.0 = 1000.0 - 200

    #: FA
    answer = mike_remaining_amount
    return answer # eval: return 800.0

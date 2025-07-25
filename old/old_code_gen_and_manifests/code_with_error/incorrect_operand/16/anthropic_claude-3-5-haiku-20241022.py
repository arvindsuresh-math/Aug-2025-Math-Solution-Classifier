def solve(
    johnson_share_ratio: int = 5,  # Johnson gets 5 parts
    mike_share_ratio: int = 2,  # Mike gets 2 parts
    johnson_amount: int = 2500,  # Johnson got $2500
    shirt_cost: int = 200  # shirt costs $200
):
    """Index: 16.
    Returns: the amount of money Mike has left after buying a shirt."""

    #: L2
    part_value = johnson_amount / johnson_share_ratio

    #: L3
    mike_total_share = johnson_share_ratio * part_value

    #: L4
    mike_remaining_amount = mike_total_share - shirt_cost

    #: FA
    answer = mike_remaining_amount
    return answer
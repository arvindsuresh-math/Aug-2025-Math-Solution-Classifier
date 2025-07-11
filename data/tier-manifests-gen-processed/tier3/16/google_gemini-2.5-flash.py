def solve():
    """Index: 16.
    Returns: the amount of money Mike has left after spending on a shirt.
    """
    # L1
    mike_ratio_part = 2 # in the ratio 2:5 respectively
    johnson_ratio_part = 5 # in the ratio 2:5 respectively

    # L2
    johnson_share = 2500 # Johnson got $2500
    value_per_part = johnson_share / johnson_ratio_part

    # L3
    mike_initial_share = mike_ratio_part * value_per_part

    # L4
    shirt_cost = 200 # a shirt that costs $200
    mike_remaining_share = mike_initial_share - shirt_cost

    # FA
    answer = mike_remaining_share
    return answer
def solve():
    """Index: 16.
    Returns: the amount Mike will have after buying the shirt.
    """
    # L2
    johnson_share = 2500 # Johnson got $2500
    johnson_ratio = 5 # ratio 2:5 respectively
    part_value = johnson_share / johnson_ratio

    # L3
    mike_ratio = 2 # Mike gets 2 parts
    mike_share = mike_ratio * part_value

    # L4
    shirt_cost = 200 # shirt that costs $200
    mike_remaining = mike_share - shirt_cost

    # FA
    answer = mike_remaining
    return answer
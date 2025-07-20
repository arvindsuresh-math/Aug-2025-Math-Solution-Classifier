def solve():
    """Index: 4514.
    Returns: the total amount Betty paid for her online order.
    """
    # L1
    num_slippers = 6 # 6 pieces of slippers
    cost_per_slipper = 2.5 # $2.5 each
    cost_slippers = num_slippers * cost_per_slipper

    # L2
    num_lipsticks = 4 # 4 pieces of lipstick
    cost_per_lipstick = 1.25 # $1.25 each
    cost_lipsticks = num_lipsticks * cost_per_lipstick

    # L3
    num_hair_color = 8 # 8 pieces of hair color
    cost_per_hair_color = 3 # $3 each
    cost_hair_color = num_hair_color * cost_per_hair_color

    # L4
    total_cost = cost_slippers + cost_lipsticks + cost_hair_color

    # FA
    answer = total_cost
    return answer
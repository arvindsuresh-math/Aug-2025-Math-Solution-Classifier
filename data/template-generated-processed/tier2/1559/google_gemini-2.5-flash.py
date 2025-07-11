def solve():
    """Index: 1559.
    Returns: the total money Maci pays for the pens.
    """
    # L1
    num_blue_pens = 10 # ten blue pens
    cost_blue_pen = 0.10 # ten cents each
    cost_blue_pens = num_blue_pens * cost_blue_pen

    # L2
    cost_red_pen_each = 2 * cost_blue_pen

    # L3
    num_red_pens = 15 # 15 red pens
    cost_red_pens = num_red_pens * cost_red_pen_each

    # L4
    total_cost = cost_red_pens + cost_blue_pens

    # FA
    answer = total_cost
    return answer
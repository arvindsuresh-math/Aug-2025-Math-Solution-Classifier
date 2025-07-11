def solve():
    """Index: 1027.
    Returns: the total amount John paid for the color drawing.
    """
    # L1
    bw_cost = 160 # black and white drawing that size would cost $160
    color_extra_percent = 0.5 # 50% more expensive
    color_extra_cost = bw_cost * color_extra_percent

    # L2
    total_cost = bw_cost + color_extra_cost

    # FA
    answer = total_cost
    return answer
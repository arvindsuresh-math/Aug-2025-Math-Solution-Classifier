def solve():
    """Index: 1027.
    Returns: the total cost John paid for the drawing.
    """
    # L1
    base_cost_bw = 160 # A black and white drawing that size would cost $160
    color_extra_percent = 0.5 # 50% more expensive
    extra_cost_coloring = base_cost_bw * color_extra_percent

    # L2
    total_cost = base_cost_bw + extra_cost_coloring

    # FA
    answer = total_cost
    return answer
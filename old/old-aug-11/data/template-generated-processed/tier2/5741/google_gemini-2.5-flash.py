def solve():
    """Index: 5741.
    Returns: the total cost for hair and nails including tip.
    """
    # L1
    hair_updo_cost = 50 # Hair updos cost $50
    tip_percent_num = 20 # 20% tip
    percent_factor = 0.01 # WK
    hair_tip = hair_updo_cost * tip_percent_num * percent_factor

    # L2
    manicure_cost = 30 # manicures cost $30
    manicure_tip = manicure_cost * tip_percent_num * percent_factor

    # L3
    total_tips = hair_tip + manicure_tip

    # L4
    base_cost_services = hair_updo_cost + manicure_cost

    # L5
    final_total_cost = base_cost_services + total_tips

    # FA
    answer = final_total_cost
    return answer
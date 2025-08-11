def solve():
    """Index: 5871.
    Returns: the total tip amount.
    """
    # L1
    children_haircut_cost = 36 # Children’s haircuts are $36
    num_daughters = 2 # her two young daughters
    daughters_total_cost = children_haircut_cost * num_daughters

    # L2
    womens_haircut_cost = 48 # Women’s haircuts are $48
    total_haircut_cost = daughters_total_cost + womens_haircut_cost

    # L3
    tip_percent_num = 20 # 20% tip
    percent_factor = 0.01 # WK
    tip_amount = total_haircut_cost * tip_percent_num * percent_factor

    # FA
    answer = tip_amount
    return answer
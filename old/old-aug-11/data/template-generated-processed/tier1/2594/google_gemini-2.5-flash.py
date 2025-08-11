def solve():
    """Index: 2594.
    Returns: the total amount John spends a month on paintballs.
    """
    # L1
    boxes_per_play = 3 # buys 3 boxes of paintballs
    cost_per_box = 25 # $25 per box
    cost_per_play = boxes_per_play * cost_per_box

    # L2
    times_per_month = 3 # 3 times a month
    total_monthly_cost = cost_per_play * times_per_month

    # FA
    answer = total_monthly_cost
    return answer
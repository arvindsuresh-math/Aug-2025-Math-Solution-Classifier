def solve():
    """Index: 2594.
    Returns: the total amount John spends per month on paintballs.
    """
    # L1
    boxes_per_session = 3 # buys 3 boxes of paintballs each time
    price_per_box = 25 # $25 per box
    cost_per_session = boxes_per_session * price_per_box

    # L2
    sessions_per_month = 3 # plays 3 times a month
    total_monthly_cost = cost_per_session * sessions_per_month

    # FA
    answer = total_monthly_cost
    return answer
def solve():
    """Index: 7127.
    Returns: the total cost of John's hats.
    """
    # L1
    num_weeks = 2 # 2 weeks
    days_per_week = 7 # WK
    num_hats = num_weeks * days_per_week

    # L2
    cost_per_hat = 50 # each hat costs $50
    total_cost = num_hats * cost_per_hat

    # FA
    answer = total_cost
    return answer
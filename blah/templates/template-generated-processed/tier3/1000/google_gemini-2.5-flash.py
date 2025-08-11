def solve():
    """Index: 1000.
    Returns: the cost per use of the heating pad.
    """
    # L1
    times_per_week = 3 # 3 times a week
    number_of_weeks = 2 # for 2 weeks
    total_uses = times_per_week * number_of_weeks

    # L2
    total_cost = 30 # $30
    cost_per_use = total_cost / total_uses

    # FA
    answer = cost_per_use
    return answer
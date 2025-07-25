def solve():
    """Index: 5003.
    Returns: the total number of beignets Sandra will eat in 16 weeks.
    """
    # L1
    beignets_per_morning = 3 # 3 beignets every morning
    days_in_week = 7 # WK
    beignets_per_week = beignets_per_morning * days_in_week

    # L2
    num_weeks = 16 # 16 weeks
    total_beignets = beignets_per_week * num_weeks

    # FA
    answer = total_beignets
    return answer
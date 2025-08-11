def solve():
    """Index: 183.
    Returns: the number of birds left in the poultry after a week.
    """
    # L1
    chickens_initial = 300 # 300 chickens
    turkeys_initial = 200 # 200 turkeys
    guinea_fowls_initial = 80 # 80 guinea fowls
    total_initial_birds = chickens_initial + turkeys_initial + guinea_fowls_initial

    # L2
    chickens_lost_per_day = 20 # lost 20 chickens
    turkeys_lost_per_day = 8 # lost 8 turkeys
    guinea_fowls_lost_per_day = 5 # lost 5 guinea fowls
    total_lost_per_day = chickens_lost_per_day + turkeys_lost_per_day + guinea_fowls_lost_per_day

    # L3
    days_in_week = 7 # WK
    total_lost_after_week = total_lost_per_day * days_in_week

    # L4
    birds_left = total_initial_birds - total_lost_after_week

    # FA
    answer = birds_left
    return answer
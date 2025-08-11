def solve():
    """Index: 183.
    Returns: the number of birds left in the poultry after a week.
    """
    # L1
    chickens = 300 # 300 chickens
    turkeys = 200 # 200 turkeys
    guinea_fowls = 80 # 80 guinea fowls
    total_birds = chickens + turkeys + guinea_fowls

    # L2
    chickens_lost_per_day = 20 # lost 20 chickens per day
    turkeys_lost_per_day = 8 # lost 8 turkeys per day
    guinea_fowls_lost_per_day = 5 # lost 5 guinea fowls per day
    birds_lost_per_day = chickens_lost_per_day + turkeys_lost_per_day + guinea_fowls_lost_per_day

    # L3
    days_in_week = 7 # a week is 7 days
    total_birds_lost = birds_lost_per_day * days_in_week

    # L4
    birds_left = total_birds - total_birds_lost

    # FA
    answer = birds_left
    return answer
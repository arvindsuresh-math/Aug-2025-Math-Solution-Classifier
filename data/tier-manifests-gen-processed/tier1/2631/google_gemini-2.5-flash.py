def solve():
    """Index: 2631.
    Returns: the total yards of fabric needed for 3 days.
    """
    # L1
    yards_per_shirt = 2 # 2 yards of fabric
    shirts_per_day_jenson = 3 # 3 shirts
    jenson_fabric_per_day = yards_per_shirt * shirts_per_day_jenson

    # L2
    yards_per_pant = 5 # 5 yards of fabric
    pants_per_day_kingsley = 5 # 5 pairs of pants
    kingsley_fabric_per_day = yards_per_pant * pants_per_day_kingsley

    # L3
    total_fabric_per_day = kingsley_fabric_per_day + jenson_fabric_per_day

    # L4
    num_days = 3 # every 3 days
    total_fabric_three_days = total_fabric_per_day * num_days

    # FA
    answer = total_fabric_three_days
    return answer
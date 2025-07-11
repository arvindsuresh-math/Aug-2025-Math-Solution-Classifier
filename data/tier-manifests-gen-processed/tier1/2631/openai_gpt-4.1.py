def solve():
    """Index: 2631.
    Returns: the total yards of fabric Jenson and Kingsley need every 3 days.
    """
    # L1
    jenson_shirts_per_day = 3 # Jenson makes 3 shirts
    yards_per_shirt = 2 # each shirt uses 2 yards of fabric
    jenson_fabric_per_day = yards_per_shirt * jenson_shirts_per_day

    # L2
    kingsley_pants_per_day = 5 # Kingsley makes 5 pairs of pants per day
    yards_per_pant = 5 # a pair of pants uses 5 yards of fabric
    kingsley_fabric_per_day = kingsley_pants_per_day * yards_per_pant

    # L3
    total_fabric_per_day = kingsley_fabric_per_day + jenson_fabric_per_day

    # L4
    num_days = 3 # every 3 days
    total_fabric_3_days = total_fabric_per_day * num_days

    # FA
    answer = total_fabric_3_days
    return answer
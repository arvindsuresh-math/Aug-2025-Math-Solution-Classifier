def solve():
    """Index: 4735.
    Returns: the total ounces of fluid Tom drinks in a week.
    """
    # L1
    soda_can_size = 12 # 12-oz cans of soda
    cans_per_day = 5 # 5 12-oz cans of soda
    soda_ounces_per_day = soda_can_size * cans_per_day

    # L2
    water_ounces_per_day = 64 # 64 ounces of water
    total_ounces_per_day = soda_ounces_per_day + water_ounces_per_day

    # L3
    days_per_week = 7 # WK
    total_ounces_per_week = total_ounces_per_day * days_per_week

    # FA
    answer = total_ounces_per_week
    return answer
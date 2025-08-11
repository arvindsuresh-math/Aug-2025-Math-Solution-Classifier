def solve():
    """Index: 6072.
    Returns: the total volume of shampoo and conditioner Sarah will use in two weeks.
    """
    # L1
    shampoo_daily_oz = 1 # 1 ounce of shampoo
    conditioner_daily_oz = 0.5 # one half as much conditioner as shampoo daily
    daily_total_volume = shampoo_daily_oz + conditioner_daily_oz

    # L2
    num_weeks = 2 # In two weeks
    days_per_week = 7 # WK
    total_days = num_weeks * days_per_week

    # L3
    total_volume_used = total_days * daily_total_volume

    # FA
    answer = total_volume_used
    return answer
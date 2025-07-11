def solve():
    """Index: 1336.
    Returns: the total hours Jason spends cutting grass.
    """
    # L1
    yards_per_day = 8 # 8 yards on both Saturday and Sunday
    number_of_days = 2 # both Saturday and Sunday
    total_yards = number_of_days * yards_per_day

    # L2
    minutes_per_yard = 30 # 30 minutes to cut 1 lawn
    total_minutes = minutes_per_yard * total_yards

    # L3
    minutes_per_hour = 60 # 60 minutes in 1 hour
    total_hours = total_minutes / minutes_per_hour

    # FA
    answer = total_hours
    return answer
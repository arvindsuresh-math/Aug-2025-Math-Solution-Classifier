def solve():
    """Index: 5643.
    Returns: the total time Aron spends cleaning each week in minutes.
    """
    # L1
    vacuuming_minutes_per_day = 30 # 30 minutes/day
    vacuuming_days_per_week = 3 # three times a week
    total_vacuuming_minutes_per_week = vacuuming_minutes_per_day * vacuuming_days_per_week

    # L2
    dusting_minutes_per_day = 20 # 20 minutes/day
    dusting_days_per_week = 2 # 2 days a week
    total_dusting_minutes_per_week = dusting_minutes_per_day * dusting_days_per_week

    # L3
    total_cleaning_minutes_per_week = total_vacuuming_minutes_per_week + total_dusting_minutes_per_week

    # FA
    answer = total_cleaning_minutes_per_week
    return answer
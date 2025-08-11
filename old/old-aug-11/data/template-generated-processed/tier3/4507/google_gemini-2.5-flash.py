def solve():
    """Index: 4507.
    Returns: the total number of hours John naps.
    """
    # L1
    total_days = 70 # In 70 days
    days_per_week = 7 # WK
    num_weeks = total_days / days_per_week

    # L2
    naps_per_week = 3 # 3 naps a week
    total_naps = num_weeks * naps_per_week

    # L3
    hours_per_nap = 2 # Each nap is 2 hours long
    total_nap_hours = total_naps * hours_per_nap

    # FA
    answer = total_nap_hours
    return answer
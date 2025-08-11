def solve():
    """Index: 1859.
    Returns: the total number of more pages Janet reads than Belinda in 6 weeks.
    """
    # L1
    num_weeks = 6 # 6 weeks
    days_per_week = 7 # WK
    total_days = num_weeks * days_per_week

    # L2
    janet_pages_per_day = 80 # Janet reads 80 pages a day
    belinda_pages_per_day = 30 # Belinda reads 30 pages a day
    daily_difference = janet_pages_per_day - belinda_pages_per_day

    # L3
    total_difference_pages = daily_difference * total_days

    # FA
    answer = total_difference_pages
    return answer
def solve():
    """Index: 6705.
    Returns: the number of pages Mark reads a week now.
    """
    # L1
    pages_per_day_before = 100 # Before he read 100 pages a day
    hours_per_day_before = 2 # He used to read 2 hours a day
    reading_speed_pages_per_hour = pages_per_day_before / hours_per_day_before

    # L2
    increase_factor = 1.5 # increased that by 150%
    increased_hours = hours_per_day_before * increase_factor

    # L3
    current_hours_per_day = hours_per_day_before + increased_hours

    # L4
    current_pages_per_day = current_hours_per_day * reading_speed_pages_per_hour

    # L5
    days_per_week = 7 # WK
    pages_per_week = current_pages_per_day * days_per_week

    # FA
    answer = pages_per_week
    return answer
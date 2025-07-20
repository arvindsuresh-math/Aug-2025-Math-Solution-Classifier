def solve():
    """Index: 3974.
    Returns: the number of weeks it will take John to read the bible.
    """
    # L1
    hours_per_day = 2 # 2 hours a day
    pages_per_hour = 50 # 50 pages an hour
    pages_per_day = hours_per_day * pages_per_hour

    # L2
    days_per_week = 7 # WK
    pages_per_week = days_per_week * pages_per_day

    # L3
    total_pages = 2800 # 2800 pages long
    weeks_to_read = total_pages / pages_per_week

    # FA
    answer = weeks_to_read
    return answer
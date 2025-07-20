def solve():
    """Index: 4718.
    Returns: the number of weeks it will take to finish the book.
    """
    # L1
    end_time_pm = 4 # from 1 PM to 4 PM
    start_time_pm = 1 # from 1 PM to 4 PM
    hours_per_day = end_time_pm - start_time_pm

    # L2
    pages_per_hour = 5 # 5 pages per hour
    pages_per_day = hours_per_day * pages_per_hour

    # L3
    total_pages = 735 # 735-page book
    total_days = total_pages / pages_per_day

    # L4
    days_per_week = 7 # WK
    total_weeks = total_days / days_per_week

    # FA
    answer = total_weeks
    return answer
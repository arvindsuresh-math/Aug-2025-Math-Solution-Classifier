def solve():
    """Index: 5827.
    Returns: the average number of more pages Ryan read per day compared to his brother.
    """
    # L1
    total_pages_ryan = 2100 # a total of 2100 pages
    days_in_a_week = 7 # finished them in a week
    ryan_avg_pages_per_day = total_pages_ryan / days_in_a_week

    # L2
    brother_pages_per_day = 200 # 200 pages each
    ryan_more_pages_per_day = ryan_avg_pages_per_day - brother_pages_per_day

    # FA
    answer = ryan_more_pages_per_day
    return answer
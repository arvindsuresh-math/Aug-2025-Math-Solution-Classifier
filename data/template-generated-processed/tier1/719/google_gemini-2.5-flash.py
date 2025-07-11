def solve():
    """Index: 719.
    Returns: the total number of visitors who went to the library that week.
    """
    # L1
    visitors_monday = 50 # 50 visitors on Monday
    tuesday_multiplier = 2 # twice that number
    visitors_tuesday = tuesday_multiplier * visitors_monday

    # L2
    total_mon_tue_visitors = visitors_tuesday + visitors_monday

    # L3
    remaining_days_count = 5 # WK
    average_visitors_other_days = 20 # an average of 20 visitors
    visitors_other_days_total = remaining_days_count * average_visitors_other_days

    # L4
    total_weekly_visitors = visitors_other_days_total + total_mon_tue_visitors

    # FA
    answer = total_weekly_visitors
    return answer
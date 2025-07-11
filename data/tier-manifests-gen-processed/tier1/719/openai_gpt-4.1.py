def solve():
    """Index: 719.
    Returns: the total number of visitors who went to the library that week.
    """
    # L1
    monday_visitors = 50 # 50 visitors on Monday
    tuesday_multiplier = 2 # twice that number
    tuesday_visitors = tuesday_multiplier * monday_visitors

    # L2
    visitors_after_tuesday = tuesday_visitors + monday_visitors

    # L3
    remaining_days = 5 # remaining days of the week
    avg_visitors_remaining = 20 # average of 20 visitors
    remaining_visitors = remaining_days * avg_visitors_remaining

    # L4
    total_visitors = remaining_visitors + visitors_after_tuesday

    # FA
    answer = total_visitors
    return answer
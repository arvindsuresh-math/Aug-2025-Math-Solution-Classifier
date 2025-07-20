def solve():
    """Index: 3512.
    Returns: the total hours Roy spent on sports in school that week.
    """
    # L1
    school_days_per_week = 5 # 5 days a week
    days_missed = 2 # missed 2 days
    days_present = school_days_per_week - days_missed

    # L2
    hours_per_day = 2 # 2 hours on sports activities
    total_hours_spent = hours_per_day * days_present

    # FA
    answer = total_hours_spent
    return answer
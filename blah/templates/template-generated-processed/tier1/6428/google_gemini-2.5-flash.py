def solve():
    """Index: 6428.
    Returns: the total hours of swimming Percy does over 4 weeks.
    """
    # L1
    before_school_hours = 1 # 1 hour before school
    after_school_hours = 1 # 1 after school
    daily_school_swim_hours = before_school_hours + after_school_hours

    # L2
    school_days_per_week = 5 # 5 days a week
    weekly_school_swim_hours = daily_school_swim_hours * school_days_per_week

    # L3
    weekend_swim_hours = 3 # 3 hours on the weekend
    total_weekly_swim_hours = weekly_school_swim_hours + weekend_swim_hours

    # L4
    num_weeks = 4 # 4 weeks
    total_swim_over_weeks = num_weeks * total_weekly_swim_hours

    # FA
    answer = total_swim_over_weeks
    return answer
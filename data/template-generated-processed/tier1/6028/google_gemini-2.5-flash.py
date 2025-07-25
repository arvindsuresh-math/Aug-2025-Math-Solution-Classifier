def solve():
    """Index: 6028.
    Returns: the total hours Bethany rode over a 2 week period.
    """
    # L1
    hours_per_weekday_session = 1 # 1 hour after school every Monday, Wednesday, and Friday
    num_weekday_sessions = 3 # every Monday, Wednesday, and Friday
    initial_hours_mon_wed_fri = hours_per_weekday_session * num_weekday_sessions

    # L2
    minutes_per_tue_thu_session = 30 # 30 min
    num_tue_thu_sessions = 2 # Tuesday and Thursday
    minutes_tue_thu = minutes_per_tue_thu_session * num_tue_thu_sessions
    minutes_per_hour = 60 # WK
    hours_tue_thu = minutes_tue_thu / minutes_per_hour

    # L3
    hours_saturday = 2 # 2 hours
    total_hours_per_week = initial_hours_mon_wed_fri + hours_tue_thu + hours_saturday

    # L4
    num_weeks = 2 # 2 week period
    total_hours_two_weeks = total_hours_per_week * num_weeks

    # FA
    answer = total_hours_two_weeks
    return answer
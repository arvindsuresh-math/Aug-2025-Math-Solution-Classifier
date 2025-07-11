def solve():
    """Index: 479.
    Returns: the total number of hours Kat trains per week.
    """
    # L1
    strength_sessions_per_week = 3 # 3 times a week doing strength training
    strength_session_duration = 1 # 1 hour in the gym
    strength_hours = strength_sessions_per_week * strength_session_duration

    # L2
    boxing_sessions_per_week = 4 # 4 times a week for boxing
    boxing_session_duration = 1.5 # 1.5 hours per boxing session
    boxing_hours = boxing_sessions_per_week * boxing_session_duration

    # L3
    total_hours = strength_hours + boxing_hours

    # FA
    answer = total_hours
    return answer
def solve():
    """Index: 5654.
    Returns: the total number of minutes Daniel practices during a whole week.
    """
    # L1
    practice_minutes_school_day = 15 # 15 minutes each day during the school week
    school_days_per_week = 5 # WK
    minutes_school_week = practice_minutes_school_day * school_days_per_week

    # L2
    weekend_practice_multiplier = 2 # practices twice as long each day on the weekend
    practice_minutes_weekend_day = practice_minutes_school_day * weekend_practice_multiplier

    # L3
    weekend_days = 2 # WK
    minutes_weekend = practice_minutes_weekend_day * weekend_days

    # L4
    total_practice_minutes_week = minutes_school_week + minutes_weekend

    # FA
    answer = total_practice_minutes_week
    return answer
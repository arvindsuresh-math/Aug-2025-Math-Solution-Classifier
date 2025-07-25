def solve():
    """Index: 861.
    Returns: the total number of toothbrushes given away in a 5-day work week.
    """
    # L1
    hours_per_day = 8 # 8 hour days
    visit_duration = 0.5 # each visit takes .5 hours
    visits_per_day = hours_per_day / visit_duration

    # L2
    work_days_per_week = 5 # 5 day work week
    visits_per_week = visits_per_day * work_days_per_week

    # L3
    toothbrushes_per_patient = 2 # 2 toothbrushes to every patient
    total_toothbrushes_per_week = visits_per_week * toothbrushes_per_patient

    # FA
    answer = total_toothbrushes_per_week
    return answer
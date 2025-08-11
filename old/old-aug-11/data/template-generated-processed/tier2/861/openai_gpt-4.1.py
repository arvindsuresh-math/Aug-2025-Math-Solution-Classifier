def solve():
    """Index: 861.
    Returns: the number of toothbrushes given in a 5 day work week.
    """
    # L1
    hours_per_day = 8 # 8 hour days
    visit_duration = 0.5 # each visit takes .5 hours
    visits_per_day = hours_per_day / visit_duration

    # L2
    days_per_week = 5 # 5 day work week
    visits_per_week = visits_per_day * days_per_week

    # L3
    toothbrushes_per_visit = 2 # gives away 2 toothbrushes to every patient
    toothbrushes_per_week = visits_per_week * toothbrushes_per_visit

    # FA
    answer = toothbrushes_per_week
    return answer
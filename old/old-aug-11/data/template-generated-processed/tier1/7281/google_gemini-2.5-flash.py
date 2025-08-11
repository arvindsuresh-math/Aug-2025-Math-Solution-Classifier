def solve():
    """Index: 7281.
    Returns: the number of minutes Indira played cricket.
    """
    # L1
    sean_minutes_per_day = 50 # 50 minutes each day
    sean_days_played = 14 # for 14 days
    sean_total_minutes = sean_minutes_per_day * sean_days_played

    # L2
    total_minutes_played = 1512 # Together they played cricket for 1512 minutes
    indira_total_minutes = total_minutes_played - sean_total_minutes

    # FA
    answer = indira_total_minutes
    return answer
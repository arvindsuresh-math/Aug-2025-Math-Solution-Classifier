def solve():
    """Index: 4601.
    Returns: the total hours Reese will practice after five months.
    """
    # L1
    hours_per_week = 4 # four hours every week
    weeks_per_month = 4 # WK
    hours_per_month = hours_per_week * weeks_per_month

    # L2
    num_months = 5 # five months
    total_practice_hours = num_months * hours_per_month

    # FA
    answer = total_practice_hours
    return answer
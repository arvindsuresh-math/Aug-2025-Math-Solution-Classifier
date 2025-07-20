def solve():
    """Index: 3429.
    Returns: the total hours Elle spends practicing piano each week.
    """
    # L1
    daily_practice_hours = 0.50 # practices piano for 30 minutes (converted to hours)
    weekday_count = 5 # From Monday to Friday
    weekday_total_practice_hours = daily_practice_hours * weekday_count

    # L2
    saturday_multiplier = 3 # practices piano three times as much as on a weekday
    saturday_practice_hours = daily_practice_hours * saturday_multiplier

    # L3
    weekly_total_practice_hours = weekday_total_practice_hours + saturday_practice_hours

    # FA
    answer = weekly_total_practice_hours
    return answer
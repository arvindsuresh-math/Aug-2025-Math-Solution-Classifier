def solve():
    """Index: 5574.
    Returns: the total hours Mike will practice until the next game.
    """
    # L1
    weekday_practice_hours = 3 # practices for 3 hours every weekday
    weekdays_per_week = 5 # WK
    weekday_total_hours = weekday_practice_hours * weekdays_per_week

    # L2
    saturday_practice_hours = 5 # on Saturdays he practices for 5 hours
    total_hours_per_week = weekday_total_hours + saturday_practice_hours

    # L3
    weeks_until_game = 3 # game in 3 weeks
    total_practice_hours = total_hours_per_week * weeks_until_game

    # FA
    answer = total_practice_hours
    return answer
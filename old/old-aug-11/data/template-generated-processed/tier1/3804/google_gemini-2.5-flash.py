def solve():
    """Index: 3804.
    Returns: the total hours of sleep Corveus lacks in a week.
    """
    # L1
    recommended_sleep_hours = 6 # doctor recommended for him to sleep 6 hours a day
    current_sleep_hours = 4 # sleeps 4 hours a day
    daily_sleep_lack = recommended_sleep_hours - current_sleep_hours

    # L2
    days_in_week = 7 # WK
    weekly_sleep_lack = daily_sleep_lack * days_in_week

    # FA
    answer = weekly_sleep_lack
    return answer
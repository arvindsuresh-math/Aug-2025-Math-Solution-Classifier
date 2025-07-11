def solve():
    """Index: 770.
    Returns: the total hours children watch television in two weeks.
    """
    # L1
    minutes_per_day = 45 # children 6–11 years old spend 45 minutes each day watching television
    allowed_days_per_week = 4 # allowed to watch television 4 days a week
    minutes_per_week = minutes_per_day * allowed_days_per_week

    # L2
    minutes_per_hour = 60 # WK
    hours_per_week = minutes_per_week / minutes_per_hour

    # L3
    number_of_weeks = 2 # 2 weeks
    total_hours_two_weeks = hours_per_week * number_of_weeks

    # FA
    answer = total_hours_two_weeks
    return answer
def solve():
    """Index: 7373.
    Returns: the total minutes Hank spends reading in 1 week.
    """
    # L1
    morning_reading_per_day_weekday = 30 # 30 minutes
    weekday_reading_days = 5 # 5 days a week
    morning_weekday_total_minutes = morning_reading_per_day_weekday * weekday_reading_days

    # L2
    weekend_reading_multiplier = 2 # doubles his reading time
    morning_reading_per_day_weekend = morning_reading_per_day_weekday * weekend_reading_multiplier

    # L3
    weekend_days = 2 # Saturday and Sundays
    morning_weekend_total_minutes = morning_reading_per_day_weekend + morning_reading_per_day_weekend

    # L4
    evening_reading_per_day_weekday_hours = 1 # 1 hour
    evening_weekday_total_hours = evening_reading_per_day_weekday_hours * weekday_reading_days

    # L5
    evening_reading_per_day_weekend_hours = evening_reading_per_day_weekday_hours * weekend_reading_multiplier

    # L6
    evening_weekend_total_hours = evening_reading_per_day_weekend_hours + evening_reading_per_day_weekend_hours

    # L7
    total_evening_reading_hours = evening_weekday_total_hours + evening_weekend_total_hours
    minutes_per_hour = 60 # WK
    total_evening_reading_minutes = total_evening_reading_hours * minutes_per_hour

    # L8
    total_reading_minutes_per_week = morning_weekday_total_minutes + morning_weekend_total_minutes + total_evening_reading_minutes

    # FA
    answer = total_reading_minutes_per_week
    return answer
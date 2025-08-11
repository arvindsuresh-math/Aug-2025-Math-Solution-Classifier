def solve():
    """Index: 486.
    Returns: the daily average rain total for the week.
    """
    # L1
    monday_morning_rain = 2 # 2 inches on Monday morning
    monday_later_rain = 1 # 1 more inch later that day
    total_monday_rain = monday_morning_rain + monday_later_rain

    # L2
    tuesday_multiplier = 2 # twice that much on Tuesday
    total_tuesday_rain = tuesday_multiplier * total_monday_rain

    # L3
    wednesday_rain = 0 # It did not rain on Wednesday
    thursday_rain = 1 # on Thursday it rained 1 inch
    total_wed_thu_rain = wednesday_rain + thursday_rain

    # L4
    total_friday_rain = total_monday_rain + total_tuesday_rain + total_wed_thu_rain

    # L5
    total_week_rain = total_monday_rain + total_tuesday_rain + total_wed_thu_rain + total_friday_rain

    # L6
    number_of_days_for_average = 5 # WK
    average_daily_rain = total_week_rain / number_of_days_for_average

    # FA
    answer = average_daily_rain
    return answer
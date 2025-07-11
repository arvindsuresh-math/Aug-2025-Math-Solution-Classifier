def solve():
    """Index: 486.
    Returns: the daily average rain total for the week in inches.
    """
    # L1
    monday_morning_rain = 2 # it rained 2 inches on Monday morning
    monday_later_rain = 1 # 1 more inch later that day
    monday_total = monday_morning_rain + monday_later_rain

    # L2
    tuesday_multiplier = 2 # it rained twice that much on Tuesday
    tuesday_total = tuesday_multiplier * monday_total

    # L3
    wednesday_rain = 0 # did not rain on Wednesday
    thursday_rain = 1 # on Thursday it rained 1 inch
    wed_thu_total = wednesday_rain + thursday_rain

    # L4
    friday_total = monday_total + tuesday_total + wed_thu_total # total was equal to Monday through Thursday combined

    # L5
    week_total = monday_total + tuesday_total + wed_thu_total + friday_total

    # L6
    days = 5 # Monday through Friday (5 days)
    average_daily_rain = week_total / days

    # FA
    answer = average_daily_rain
    return answer
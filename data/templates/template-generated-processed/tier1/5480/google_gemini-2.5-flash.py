def solve():
    """Index: 5480.
    Returns: the total number of articles Helga was able to write this week.
    """
    # L1
    articles_per_30_min = 5 # 5 articles every 30 minutes
    minutes_in_half_hour = 30 # WK
    minutes_per_hour = 60 # WK
    multiplier_for_articles_per_hour = minutes_per_hour / minutes_in_half_hour # WK
    articles_per_hour = articles_per_30_min * multiplier_for_articles_per_hour

    # L2
    daily_work_hours = 4 # works 4 hours a day
    articles_per_day_usual = articles_per_hour * daily_work_hours

    # L3
    usual_work_days_per_week = 5 # 5 days a week
    articles_per_week_usual = articles_per_day_usual * usual_work_days_per_week

    # L4
    extra_hours_thursday = 2 # extra 2 hours last Thursday
    articles_extra_thursday = articles_per_hour * extra_hours_thursday

    # L5
    extra_hours_friday = 3 # extra 3 hours last Friday
    articles_extra_friday = articles_per_hour * extra_hours_friday

    # L6
    total_extra_articles = articles_extra_thursday + articles_extra_friday

    # L7
    total_articles_this_week = articles_per_week_usual + total_extra_articles

    # FA
    answer = total_articles_this_week
    return answer
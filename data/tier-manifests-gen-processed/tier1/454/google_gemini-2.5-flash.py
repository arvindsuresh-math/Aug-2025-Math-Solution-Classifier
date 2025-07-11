def solve():
    """Index: 454.
    Returns: the number of minutes of advertising in the newscast.
    """
    # L1
    national_news_minutes = 12 # 12 minutes of national news
    international_news_minutes = 5 # 5 minutes of international news
    sports_minutes = 5 # 5 minutes of sports
    weather_minutes = 2 # 2 minutes of weather forecasts
    accounted_minutes = national_news_minutes + international_news_minutes + sports_minutes + weather_minutes

    # L2
    total_newscast_minutes = 30 # half-hour newscast
    advertising_minutes = total_newscast_minutes - accounted_minutes

    # FA
    answer = advertising_minutes
    return answer
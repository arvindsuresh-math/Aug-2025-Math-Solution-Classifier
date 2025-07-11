def solve():
    """Index: 454.
    Returns: the number of minutes of advertising in the newscast.
    """
    # L1
    national_news = 12 # 12 minutes of national news
    international_news = 5 # 5 minutes of international news
    sports = 5 # 5 minutes of sports
    weather = 2 # 2 minutes of weather forecasts
    accounted_for = national_news + international_news + sports + weather

    # L2
    total_newscast = 30 # half-hour newscast
    ads = total_newscast - accounted_for

    # FA
    answer = ads
    return answer
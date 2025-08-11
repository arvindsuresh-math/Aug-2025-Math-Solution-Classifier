def solve():
    """Index: 4631.
    Returns: the expected earnings per hour.
    """
    # L1
    total_hours = 4 # in the next 4 hours
    minutes_per_hour = 60 # WK
    total_minutes = total_hours * minutes_per_hour

    # L2
    words_per_minute = 10 # She averages 10 words a minute
    total_words = total_minutes * words_per_minute

    # L3
    earnings_per_word = 0.1 # She earns $.1 per word
    earnings_from_words = total_words * earnings_per_word

    # L4
    num_articles = 3 # finish three stories
    earnings_per_article = 60 # She earns $60 per article
    earnings_from_articles = num_articles * earnings_per_article

    # L5
    total_earnings = earnings_from_words + earnings_from_articles

    # L6
    average_earnings_per_hour = total_earnings / total_hours

    # FA
    answer = average_earnings_per_hour
    return answer
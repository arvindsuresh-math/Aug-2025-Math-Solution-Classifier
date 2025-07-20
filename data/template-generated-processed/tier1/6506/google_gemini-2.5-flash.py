def solve():
    """Index: 6506.
    Returns: the total number of times Polly the parakeet will tweet.
    """
    # L1
    happy_minutes = 20 # happy for 20 minutes
    happy_tweets_per_minute = 18 # tweets 18 times per minute
    total_happy_tweets = happy_minutes * happy_tweets_per_minute

    # L2
    hungry_minutes = 20 # hungry for 20 minutes
    hungry_tweets_per_minute = 4 # tweets 4 times per minute
    total_hungry_tweets = hungry_minutes * hungry_tweets_per_minute

    # L3
    reflection_minutes = 20 # watches her reflection for 20 minutes
    reflection_tweets_per_minute = 45 # tweets 45 times per minute
    total_reflection_tweets = reflection_minutes * reflection_tweets_per_minute

    # L4
    total_tweets = total_happy_tweets + total_hungry_tweets + total_reflection_tweets

    # FA
    answer = total_tweets
    return answer
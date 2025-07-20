def solve():
    """Index: 3644.
    Returns: the total number of followers Malcolm has on all his social media.
    """
    # L1
    instagram_followers = 240 # 240 followers on Instagram
    facebook_followers = 500 # 500 followers on Facebook
    instagram_facebook_combined = instagram_followers + facebook_followers

    # L2
    twitter_divisor = 2 # half the number of followers
    twitter_followers = instagram_facebook_combined / twitter_divisor

    # L3
    tiktok_multiplier = 3 # 3 times the number of followers is has on Twitter
    tiktok_followers = twitter_followers * tiktok_multiplier

    # L4
    youtube_additional = 510 # 510 more followers on Youtube
    youtube_followers = tiktok_followers + youtube_additional

    # L5
    total_followers = instagram_facebook_combined + twitter_followers + tiktok_followers + youtube_followers

    # FA
    answer = total_followers
    return answer
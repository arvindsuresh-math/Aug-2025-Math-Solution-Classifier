def solve():
    """Index: 1451.
    Returns: the number of followers Denny will have after a year if 20000 people unfollowed him.
    """
    # L1
    days_in_year = 365 # WK
    new_followers_per_day = 1000 # gets 1000 new followers every day
    new_followers_year = days_in_year * new_followers_per_day

    # L2
    initial_followers = 100000 # has 100000 followers
    total_followers_year = initial_followers + new_followers_year

    # L3
    unfollowed = 20000 # 20000 people unfollowed him in a year
    followers_remaining = total_followers_year - unfollowed

    # FA
    answer = followers_remaining
    return answer
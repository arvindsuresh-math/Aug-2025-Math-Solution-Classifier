def solve():
    """Index: 1451.
    Returns: the total number of followers Denny will have after a year, considering new followers and unfollows.
    """
    # L1
    days_in_year = 365 # WK
    new_followers_per_day = 1000 # 1000 new followers every day
    new_followers_per_year = days_in_year * new_followers_per_day

    # L2
    initial_followers = 100000 # 100000 followers
    total_followers_before_unfollows = initial_followers + new_followers_per_year

    # L3
    unfollowed_people = 20000 # 20000 people unfollowed him
    final_followers = total_followers_before_unfollows - unfollowed_people

    # FA
    answer = final_followers
    return answer
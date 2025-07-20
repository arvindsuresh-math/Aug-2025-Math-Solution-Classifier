def solve():
    """Index: 5089.
    Returns: the number of sharks in Cape May.
    """
    # L1
    daytona_sharks = 12 # Daytona Beach has 12 sharks
    multiplier_twice = 2 # twice as many sharks
    twice_daytona_sharks = daytona_sharks * multiplier_twice

    # L2
    cape_may_more = 8 # 8 more than twice as many sharks
    cape_may_sharks = twice_daytona_sharks + cape_may_more

    # FA
    answer = cape_may_sharks
    return answer
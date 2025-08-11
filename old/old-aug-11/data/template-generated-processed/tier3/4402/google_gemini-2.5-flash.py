def solve():
    """Index: 4402.
    Returns: the total number of cookies Zach had at the end of the three days.
    """
    # L1
    cookies_monday = 32 # On Monday he baked 32 cookies
    half_divisor = 2 # only bake half of the number of cookies
    cookies_tuesday = cookies_monday / half_divisor

    # L2
    wednesday_multiplier = 3 # three times the number of cookies
    cookies_wednesday = cookies_tuesday * wednesday_multiplier

    # L3
    total_cookies_before_eating = cookies_monday + cookies_tuesday + cookies_wednesday

    # L4
    cookies_eaten_by_brother = 4 # his brother ate 4 of those cookies
    cookies_at_end = total_cookies_before_eating - cookies_eaten_by_brother

    # FA
    answer = cookies_at_end
    return answer
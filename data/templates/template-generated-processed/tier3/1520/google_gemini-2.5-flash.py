def solve():
    """Index: 1520.
    Returns: the number of cookies left for Monica.
    """
    # L1
    father_cookies = 10 # Her father ate 10 cookies
    half_divisor = 2 # half as much as the father
    mother_cookies = father_cookies / half_divisor

    # L2
    brother_additional_cookies = 2 # ate 2 more than her mother
    brother_cookies = mother_cookies + brother_additional_cookies

    # L3
    total_cookies_made = 30 # she made 30 cookies in total
    monica_cookies_left = total_cookies_made - brother_cookies - mother_cookies - father_cookies

    # FA
    answer = monica_cookies_left
    return answer
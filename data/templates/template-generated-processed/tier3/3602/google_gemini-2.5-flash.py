def solve():
    """Index: 3602.
    Returns: the number of days the box of cookies will last.
    """
    # L1
    oldest_son_cookies = 4 # oldest son gets 4 cookies
    youngest_son_cookies = 2 # youngest son gets 2 cookies
    daily_consumption = oldest_son_cookies + youngest_son_cookies

    # L2
    total_cookies_in_box = 54 # 54 cookies in a box
    days_box_lasts = total_cookies_in_box / daily_consumption

    # FA
    answer = days_box_lasts
    return answer
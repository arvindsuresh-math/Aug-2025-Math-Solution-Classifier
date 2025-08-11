from fractions import Fraction

def solve():
    """Index: 299.
    Returns: the number of boxes Basil will need to last for 30 days.
    """
    # L1
    morning_cookie = Fraction(1, 2) # 1/2 of a dog cookie in the morning
    bedtime_cookie = Fraction(1, 2) # 1/2 of a dog cookie before bed
    total_half_cookies = morning_cookie + bedtime_cookie

    # L2
    daytime_cookies = 2 # 2 whole cookies during the day
    total_daily_cookies = daytime_cookies + total_half_cookies

    # L3
    days = 30 # 30 days
    total_cookies_needed = days * total_daily_cookies

    # L4
    cookies_per_box = 45 # 45 cookies per box
    boxes_needed = total_cookies_needed / cookies_per_box

    # FA
    answer = boxes_needed
    return answer
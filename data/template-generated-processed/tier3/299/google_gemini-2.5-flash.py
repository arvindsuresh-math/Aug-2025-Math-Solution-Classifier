from fractions import Fraction

def solve():
    """Index: 299.
    Returns: the number of boxes Basil needs.
    """
    # L1
    morning_fraction = Fraction(1, 2) # 1/2 of a dog cookie in the morning
    bedtime_fraction = Fraction(1, 2) # and before bed
    daily_fractional_cookies = morning_fraction + bedtime_fraction

    # L2
    daytime_whole_cookies = 2 # 2 whole cookies during the day
    total_daily_cookies = daytime_whole_cookies + daily_fractional_cookies

    # L3
    number_of_days = 30 # last her for 30 days
    total_cookies_needed = number_of_days * total_daily_cookies

    # L4
    cookies_per_box = 45 # 45 cookies per box
    boxes_needed = total_cookies_needed / cookies_per_box

    # FA
    answer = boxes_needed
    return answer
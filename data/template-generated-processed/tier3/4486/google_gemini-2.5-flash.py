from fractions import Fraction

def solve():
    """Index: 4486.
    Returns: the total number of cookies Annie ate during these three days.
    """
    # L1
    cookies_monday = 5 # She ate 5 cookies on Monday
    tuesday_multiplier = 2 # two times more on Tuesday
    cookies_tuesday = cookies_monday * tuesday_multiplier

    # L2
    wednesday_percentage = Fraction(40, 100) # 40% more on Wednesday
    additional_cookies_wednesday = wednesday_percentage * cookies_tuesday

    # L3
    cookies_wednesday = cookies_tuesday + additional_cookies_wednesday

    # L4
    total_cookies = cookies_monday + cookies_tuesday + cookies_wednesday

    # FA
    answer = total_cookies
    return answer
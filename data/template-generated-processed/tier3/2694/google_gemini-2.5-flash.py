def solve():
    """Index: 2694.
    Returns: the number of cookies Frank has.
    """
    # L1
    millie_cookies = 4 # If Millie has 4 cookies
    mike_multiplier = 3 # three times as many cookies as Millie
    mike_cookies = millie_cookies * mike_multiplier

    # L2
    half_divisor = 2 # half the number of cookies
    less_than_value = 3 # three less than
    frank_cookies = mike_cookies / half_divisor - less_than_value

    # FA
    answer = frank_cookies
    return answer
from fractions import Fraction

def solve():
    """Index: 7167.
    Returns: the number of cookies Maria will have left.
    """
    # L1
    initial_cookies = 19 # Maria has 19 cookies
    given_to_friend = 5 # give her friend 5 of them
    cookies_after_friend = initial_cookies - given_to_friend

    # L2
    half_divisor = 2 # half of the rest
    cookies_after_family = cookies_after_friend / half_divisor

    # L3
    eaten_numerator = 2 # Maria decided to eat 2 cookies
    cookies_eaten = Fraction(eaten_numerator, cookies_after_family) * cookies_after_family

    # L4
    cookies_left = cookies_after_family - cookies_eaten

    # FA
    answer = cookies_left
    return answer
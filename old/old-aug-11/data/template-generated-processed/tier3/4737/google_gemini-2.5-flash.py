from fractions import Fraction

def solve():
    """Index: 4737.
    Returns: the total number of cookies remaining in the jar.
    """
    # L1
    white_cookies_eaten_fraction = Fraction(3, 4) # 3/4 of the white cookies
    initial_white_cookies = 80 # initially had 80 white cookies
    eaten_white_cookies = white_cookies_eaten_fraction * initial_white_cookies

    # L2
    remaining_white_cookies = initial_white_cookies - eaten_white_cookies

    # L3
    more_black_cookies = 50 # 50 more black cookies
    initial_black_cookies = initial_white_cookies + more_black_cookies

    # L4
    black_cookies_eaten_fraction = Fraction(1, 2) # half of the black cookies
    eaten_black_cookies = black_cookies_eaten_fraction * initial_black_cookies

    # L5
    remaining_black_cookies = initial_black_cookies - eaten_black_cookies

    # L6
    total_remaining_cookies = remaining_black_cookies + remaining_white_cookies

    # FA
    answer = total_remaining_cookies
    return answer
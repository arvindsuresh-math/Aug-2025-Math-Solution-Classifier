from fractions import Fraction

def solve():
    """Index: 1097.
    Returns: the number of cookies that were not eaten.
    """
    # L1
    initial_cookies = 200 # Out of the 200 cookies
    wife_percentage = Fraction(30, 100) # his wife took 30%
    wife_ate_cookies = wife_percentage * initial_cookies

    # L2
    cookies_after_wife = initial_cookies - wife_ate_cookies

    # L3
    daughter_ate_cookies = 40 # his daughter took 40 from the remaining cookies
    cookies_after_daughter = cookies_after_wife - daughter_ate_cookies

    # L4
    javier_fraction = Fraction(1, 2) # he ate half of the remaining cookies
    javier_ate_cookies = javier_fraction * cookies_after_daughter

    # L5
    cookies_remaining = cookies_after_daughter - javier_ate_cookies

    # FA
    answer = cookies_remaining
    return answer
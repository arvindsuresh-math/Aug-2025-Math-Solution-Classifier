from fractions import Fraction

def solve():
    """Index: 3864.
    Returns: the number of cookies left for Neil.
    """
    # L1
    total_cookies = 20 # Neil baked 20 cookies
    fraction_given = Fraction(2, 5) # 2/5 of the cookies
    cookies_given = total_cookies * fraction_given

    # L2
    cookies_left = total_cookies - cookies_given

    # FA
    answer = cookies_left
    return answer
from fractions import Fraction

def solve():
    """Index: 704.
    Returns: the number of cookies left with Sabrina.
    """
    # L1
    initial_cookies = 20 # Sabrina had 20 cookies at the start
    given_to_brother = 10 # gave 10 cookies to her brother
    cookies_after_brother = initial_cookies - given_to_brother

    # L2
    mother_divisor = 2 # half the number of cookies she gave her brother
    received_from_mother = given_to_brother / mother_divisor

    # L3
    cookies_before_sister = cookies_after_brother + received_from_mother

    # L4
    sister_fraction = Fraction(2, 3) # two-thirds of her cookies
    given_to_sister = cookies_before_sister * sister_fraction

    # L5
    cookies_left = cookies_before_sister - given_to_sister

    # FA
    answer = cookies_left
    return answer
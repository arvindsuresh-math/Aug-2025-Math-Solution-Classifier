from fractions import Fraction

def solve():
    """Index: 4040.
    Returns: the number of cookies each child gets.
    """
    # L1
    adult_fraction = Fraction(1, 3) # adults eat 1/3 of the cookies
    total_cookies = 120 # a total of 120 cookies
    cookies_eaten_by_adults = adult_fraction * total_cookies

    # L2
    remaining_cookies = total_cookies - cookies_eaten_by_adults

    # L3
    num_children = 4 # four children
    cookies_per_child = remaining_cookies / num_children

    # FA
    answer = cookies_per_child
    return answer
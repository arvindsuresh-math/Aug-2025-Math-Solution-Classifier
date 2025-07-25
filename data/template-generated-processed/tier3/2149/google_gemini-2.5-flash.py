from fractions import Fraction

def solve():
    """Index: 2149.
    Returns: the number of boys who play theater with Ocho.
    """
    # L1
    girls_fraction = Fraction(1, 2) # half are girls
    total_fraction_of_friends = 1 # WK
    boys_fraction = total_fraction_of_friends - girls_fraction

    # L2
    total_friends = 8 # Ocho has 8 friends
    boys_playing_theater = total_friends * boys_fraction

    # FA
    answer = boys_playing_theater
    return answer
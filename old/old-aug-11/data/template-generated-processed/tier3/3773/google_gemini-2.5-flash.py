from fractions import Fraction

def solve():
    """Index: 3773.
    Returns: the number of sweets still in the packet.
    """
    # L1
    cherry_sweets = 30 # 30 cherry-flavored sweets
    strawberry_sweets = 40 # 40 strawberry-flavored sweets
    pineapple_sweets = 50 # 50 pineapple-flavored sweets
    eaten_fraction = Fraction(1, 2) # half of each of the flavored sweets
    sweets_eaten_by_aaron = eaten_fraction * cherry_sweets + eaten_fraction * strawberry_sweets + eaten_fraction * pineapple_sweets

    initial_total_sweets = cherry_sweets + strawberry_sweets + pineapple_sweets
    sweets_after_aaron_eats = initial_total_sweets - sweets_eaten_by_aaron

    # L2
    given_to_friend = 5 # gives 5 cherry-flavored sweets to his friend
    sweets_remaining = sweets_after_aaron_eats - given_to_friend

    # FA
    answer = sweets_remaining
    return answer
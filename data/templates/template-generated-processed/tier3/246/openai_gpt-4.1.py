from fractions import Fraction

def solve():
    """Index: 246.
    Returns: the amount of money each boy receives.
    """
    # L1
    boys_ratio = 5 # ratio of boys
    girls_ratio = 7 # ratio of girls
    total_ratio = boys_ratio + girls_ratio

    # L2
    total_children = 180 # total number of children in the family
    boys_fraction = Fraction(boys_ratio, total_ratio)
    number_of_boys = boys_fraction * total_children

    # L3
    total_money = 3900 # boys are given $3900 to share
    each_boy_receives = total_money / number_of_boys

    # FA
    answer = each_boy_receives
    return answer
from fractions import Fraction

def solve():
    """Index: 246.
    Returns: the amount of money each boy receives.
    """
    # L1
    boys_ratio_part = 5 # The ratio of boys to girls in a family is 5:7
    girls_ratio_part = 7 # The ratio of boys to girls in a family is 5:7
    total_ratio_parts = boys_ratio_part + girls_ratio_part

    # L2
    boys_fraction = Fraction(5, 12) # 5/12 represent the number of boys
    total_children = 180 # The total number of children in the family is 180
    number_of_boys = boys_fraction * total_children

    # L3
    total_money_for_boys = 3900 # If the boys are given $3900 to share
    money_per_boy = total_money_for_boys / number_of_boys

    # FA
    answer = money_per_boy
    return answer
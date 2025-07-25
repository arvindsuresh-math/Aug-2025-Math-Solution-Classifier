from fractions import Fraction

def solve():
    """Index: 6643.
    Returns: the total number of puppies Yuri has.
    """
    # L1
    second_week_fraction = Fraction(2, 5) # 2/5 times as many puppies as the first week
    first_week_puppies = 20 # The first week he adopted 20 puppies
    second_week_puppies = second_week_fraction * first_week_puppies

    # L2
    third_week_multiplier = 2 # twice the number of puppies he adopted in the second week
    third_week_puppies = third_week_multiplier * second_week_puppies

    # L3
    fourth_week_additional = 10 # ten more puppies than he adopted on the first week
    fourth_week_puppies = fourth_week_additional + first_week_puppies

    # L4
    total_puppies = fourth_week_puppies + third_week_puppies + second_week_puppies + first_week_puppies

    # FA
    answer = total_puppies
    return answer
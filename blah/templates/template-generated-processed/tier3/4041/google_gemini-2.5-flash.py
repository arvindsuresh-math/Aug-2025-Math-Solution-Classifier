from fractions import Fraction

def solve():
    """Index: 4041.
    Returns: the number of oranges the friend gets.
    """
    # L1
    total_oranges = 12 # A boy has 12 oranges
    brother_fraction_numerator = 1 # one-third of this number
    brother_fraction_denominator = 3 # one-third of this number
    oranges_given_to_brother = total_oranges * Fraction(brother_fraction_numerator, brother_fraction_denominator)

    # L2
    oranges_remaining_after_brother = total_oranges - oranges_given_to_brother

    # L3
    friend_fraction_numerator = 1 # one-fourth of the remainder
    friend_fraction_denominator = 4 # one-fourth of the remainder
    oranges_given_to_friend = oranges_remaining_after_brother * Fraction(friend_fraction_numerator, friend_fraction_denominator)

    # FA
    answer = oranges_given_to_friend
    return answer
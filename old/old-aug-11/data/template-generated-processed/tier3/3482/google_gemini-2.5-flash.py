from fractions import Fraction

def solve():
    """Index: 3482.
    Returns: the number of cotton candies left.
    """
    # L1
    candies_per_sibling = 5 # gave her brother and sister 5 cotton candies each
    num_siblings = 2 # brother and sister
    candies_given_to_siblings = candies_per_sibling * num_siblings

    # L2
    initial_cotton_candies = 50 # bought 50 cotton candies
    candies_after_siblings = initial_cotton_candies - candies_given_to_siblings

    # L3
    cousin_fraction = Fraction(1, 4) # remaining one-fourth of them to her cousin
    candies_given_to_cousin = cousin_fraction * candies_after_siblings

    # L4
    candies_after_cousin = candies_after_siblings - candies_given_to_cousin

    # L5
    candies_eaten = 12 # she ate 12 cotton candies
    remaining_candies = candies_after_cousin - candies_eaten

    # FA
    answer = remaining_candies
    return answer